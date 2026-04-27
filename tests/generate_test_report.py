import os
import sys
import subprocess
import datetime

TEST_SCRIPTS = [
    "tests/test_logins.py",
    "tests/robust_role_test.py",
    "tests/test_recovery_flow.py",
    "tests/test_record_soft_delete.py",
    "tests/test_restore_flow.py",
    "tests/check_users_roles.py"
]

def main():
    report_file = os.path.join("tests", f"Testing_Report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.md")
    print(f"Generating Test Report: {report_file}")

    markdown_tables = []
    detailed_logs = []

    for script in TEST_SCRIPTS:
        if not os.path.exists(script): continue
            
        print(f"Running {script}...")
        try:
            result = subprocess.run([sys.executable, script], capture_output=True, text=True, check=False)
            stdout_lines = result.stdout.split('\n')
            
            table_rows = []
            clean_stdout = []
            
            for line in stdout_lines:
                if line.startswith("__TEST_RESULT__||"):
                    parts = line.split("||")
                    if len(parts) == 6:
                        _, scenario, action, expected, actual, status = parts
                        icon = "✅ PASS" if status == "PASS" else "❌ FAIL"
                        table_rows.append(f"| {scenario} | {action} | {expected} | {actual} | {icon} |")
                else:
                    clean_stdout.append(line)
            
            if table_rows:
                script_name = os.path.basename(script).replace('.py', '')
                markdown_tables.append(f"### Test Target: `{script_name}`\n")
                markdown_tables.append("| Scenario | Action / Input | Expected | Actual | Result |")
                markdown_tables.append("|---|---|---|---|---|")
                markdown_tables.extend(table_rows)
                markdown_tables.append("\n")

            detailed_logs.append({
                "script": script,
                "status": "✅ PASS" if result.returncode == 0 else f"❌ FAIL (Exit Code {result.returncode})",
                "stdout": "\n".join(clean_stdout),
                "stderr": result.stderr
            })

        except Exception as e:
            print(f"Error running {script}: {e}")

    with open(report_file, "w", encoding="utf-8") as rf:
        rf.write("# LIMS - AUTOMATED TESTING REPORT\n\n")
        rf.write(f"**Date/Time:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        rf.write("## 1. System Test Cases Summary\n\n")
        if not markdown_tables:
            rf.write("*No test cases recorded.*\n\n")
        for line in markdown_tables:
            rf.write(line + "\n")
            
        rf.write("---\n\n")
        rf.write("## 2. Detailed Execution Logs\n\n")
        for log in detailed_logs:
            rf.write(f"### {log['script']}\n\n")
            rf.write(f"**Script Exit Status:** {log['status']}\n\n")
            
            out_str = log["stdout"].strip()
            if out_str:
                rf.write("**Standard Output:**\n```text\n" + out_str + "\n```\n\n")
                
            err_str = log["stderr"].strip()
            if err_str:
                rf.write("**Errors/Warnings:**\n```text\n" + err_str + "\n```\n\n")
            
            rf.write("---\n\n")
            
    print(f"\nDone! Test report saved to: {report_file}")

if __name__ == "__main__":
    main()