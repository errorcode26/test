
import os
import sys
import json

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from report_generator import generate_property_card_pdf, generate_village_excel

def test_report_generation():
    print("--- Starting Report Generation Test ---")
    
    # Ensure test_output directory exists
    output_dir = os.path.join(os.path.dirname(__file__), 'test_output')
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Sample Data with different Land Uses to test Multipliers
    test_records = [
        {
            "_id": "rec-001",
            "ulpin": "AS1801KAM001",
            "khasra_no": "101",
            "khata_no": "202",
            "location": {"state": "Assam", "district": "Kamrup", "village": "Amingaon"},
            "attributes": {"area_ha": 2.5, "land_use": "Commercial", "circle_rate_inr": 500000},
            "owner": {"name": "Arjun Sharma", "share_pct": 100, "aadhaar_mask": "XXXX-XXXX-1234"},
            "geometry": {"type": "Polygon", "coordinates": [[[91.70, 26.10], [91.71, 26.10], [91.71, 26.11], [91.70, 26.11], [91.70, 26.10]]]},
            "mutation_history": []
        },
        {
            "_id": "rec-002",
            "ulpin": "AS1801KAM002",
            "khasra_no": "102",
            "khata_no": "203",
            "location": {"state": "Assam", "district": "Kamrup", "village": "Amingaon"},
            "attributes": {"area_ha": 1.2, "land_use": "Agricultural", "circle_rate_inr": 100000},
            "owner": {"name": "Laxmi Devi", "share_pct": 100, "aadhaar_mask": "XXXX-XXXX-5678"},
            "geometry": {"type": "Polygon", "coordinates": [[[91.72, 26.12], [91.73, 26.12], [91.73, 26.13], [91.72, 26.13], [91.72, 26.12]]]},
            "mutation_history": []
        }
    ]
    
    # 2. Generate PDF for each record
    for rec in test_records:
        print(f"Generating PDF for {rec['ulpin']} ({rec['attributes']['land_use']})...")
        try:
            pdf_bytes = generate_property_card_pdf(rec)
            filename = f"Property_Card_{rec['ulpin']}.pdf"
            filepath = os.path.join(output_dir, filename)
            with open(filepath, 'wb') as f:
                f.write(pdf_bytes)
            print(f"DONE Saved to {filepath}")
        except Exception as e:
            print(f"FAIL Error generating PDF: {e}")
            
    # 3. Generate Village Ledger (Excel)
    print("Generating Village Ledger (Excel) for Amingaon...")
    try:
        excel_bytes = generate_village_excel(test_records)
        filename = "Village_Ledger_Amingaon.xlsx"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'wb') as f:
            f.write(excel_bytes)
        print(f"DONE Saved to {filepath}")
    except Exception as e:
        print(f"FAIL Error generating Excel: {e}")
        
    print("\n--- Report Generation Test Complete ---")
    print(f"Results are in: {output_dir}")

if __name__ == "__main__":
    test_report_generation()
