**PROJECT REPORT**

on

**Land Information Management System (LIMS)**

**Submitted by:**

Student Name

**University:**

University name

**Department:**

Department of Computer Science & Engineering

**Degree:**

Bachelor of Technology (B.Tech)

**Session:**

2023–2027

**University**

2025

**CERTIFICATE**

This is to certify that the project report entitled "Land Information Management System (LIMS)" submitted by Student Name, bearing Roll No. XXXXXXX, in partial fulfillment of the requirements for the award of the degree of Bachelor of Technology (B.Tech) in Computer Science & Engineering at University is a bonafide record of the work carried out by the candidate under my supervision and guidance.

The contents of this report, in full or in parts, have not been submitted to any other university or institution for the award of any degree, diploma, or fellowship.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Supervisor Name**

Department of Computer Science & Engineering

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date:

**TABLE OF CONTENTS**

[**CHAPTER 1: INTRODUCTION** 8](#_Toc228217745)

[**1.1 Problem Statement** 8](#_Toc228217746)

[**1.2 Proposed System** 8](#_Toc228217747)

[**1.3 Objectives** 9](#_Toc228217748)

[**CHAPTER 2: SDLC MODEL** 10](#_Toc228217749)

[**2.1 Software Development Life Cycle** 10](#_Toc228217750)

[**2.2 Iterative and Incremental Model** 10](#_Toc228217751)

[**2.3 SDLC Phases** 11](#_Toc228217752)

[**2.4 Iteration Plan** 12](#_Toc228217753)

[**CHAPTER 3: REQUIREMENTS ANALYSIS** 13](#_Toc228217754)

[**3.1 Functional Requirements** 13](#_Toc228217755)

[**3.2 Non-Functional Requirements** 14](#_Toc228217756)

[**CHAPTER 4: SYSTEM DESIGN** 15](#_Toc228217757)

[**4.1 Context-Level Data Flow Diagram** 15](#_Toc228217758)

[**4.2 Level-1 DFD** 16](#_Toc228217759)

[**4.3 Level-2 DFD for Mutation Processing** 17](#_Toc228217760)

[**4.4 Entity-Relationship Diagram** 17](#_Toc228217761)

[**4.5 Use Case Diagram** 19](#_Toc228217762)

[**4.6 Class Diagram** 20](#_Toc228217763)

[**4.7 Object Diagram** 21](#_Toc228217764)

[**4.8 Sequence Diagram** 22](#_Toc228217765)

[**4.9 Activity Diagram - Ownership Mutation Workflow** 23](#_Toc228217766)

[**4.10 Activity Diagram - User Login Flow** 24](#_Toc228217767)

[**4.11 PDF Property Card Generation Flow** 25](#_Toc228217768)

[**CHAPTER 5: SECURITY ARCHITECTURE** 26](#_Toc228217769)

[**5.1 Role-Based Access Control (RBAC)** 26](#_Toc228217770)

[**5.2 CAPTCHA Implementation** 28](#_Toc228217771)

[**5.3 Password Security** 29](#_Toc228217772)

[**5.4 Session Management** 29](#_Toc228217773)

[**CHAPTER 6: IMPLEMENTATION** 30](#_Toc228217774)

[**6.1 Technology Stack** 30](#_Toc228217775)

[**6.2 Database Schema - Users Collection** 31](#_Toc228217776)

[**6.3 Database Schema - Land Records Collection** 31](#_Toc228217777)

[**6.4 Database Schema - Audit Log Collection** 32](#_Toc228217778)

[**6.5 Revenue Calculation Engine** 33](#_Toc228217779)

[**6.6 API Documentation** 34](#_Toc228217780)

[**6.7 CAPTCHA Generation Module** 35](#_Toc228217781)

[**6.8 Geodesic Area Computation** 35](#_Toc228217782)

[**6.9 Ownership Mutation Processing** 36](#_Toc228217783)

[**CHAPTER 7: TESTING** 38](#_Toc228217784)

[**7.1 Testing Strategy** 38](#_Toc228217785)

[**7.2 Test Results** 38](#_Toc228217786)

[**7.3 Soft-Delete Test Verification** 39](#_Toc228217787)

[**CHAPTER 8: DEPLOYMENT** 40](#_Toc228217788)

[**8.1 Cloud Deployment on Render** 40](#_Toc228217789)

[**8.2 Standalone Executable with PyInstaller** 40](#_Toc228217790)

[**CHAPTER 9: USER MANUAL** 42](#_Toc228217791)

[**9.1 Public Viewer Workflow** 42](#_Toc228217792)

[**9.2 Revenue Officer Workflow** 42](#_Toc228217793)

[**9.3 System Administrator Workflow** 43](#_Toc228217794)

[**CHAPTER 10: OUTPUT** 44](#_Toc228217795)

[**10.1 System Screenshots** 44](#_Toc228217796)

[**10.2 Generated Documents** 44](#_Toc228217797)

[**CHAPTER 11: CONCLUSION** 45](#_Toc228217798)

[**11.1 Conclusion** 45](#_Toc228217799)

[**11.2 Limitations** 45](#_Toc228217800)

[**11.3 Future Work** 46](#_Toc228217801)

**LIST OF FIGURES**

**Figure No.**

**Title**

Figure 2.1

Iterative and Incremental SDLC Model

Figure 2.2

SDLC Phases Overview

Figure 4.1

Context-Level Data Flow Diagram

Figure 4.2

Level-1 DFD

Figure 4.3

Level-2 DFD for Mutation Processing

Figure 4.4

Entity-Relationship Diagram

Figure 4.5

Use Case Diagram

Figure 4.6

Class Diagram

Figure 4.7

Object Diagram

Figure 4.8

Sequence Diagram

Figure 4.9

Activity Diagram - Ownership Mutation Workflow

Figure 4.10

Activity Diagram - User Login Flow

Figure 4.11

PDF Property Card Generation Flow

Figure 5.1

RBAC Permission Tiers

Figure 5.2

CAPTCHA Generation and Validation Lifecycle

Figure 5.3

Password Hashing and Verification Flow

Figure 8.1

Cloud Deployment Architecture on Render

Figure 8.2

PyInstaller Executable Packaging Workflow

Figure 10.1

System Login Interface

Figure 10.2

GIS Interactive Land Parcel Viewer

**LIST OF TABLES**

**Table No.**

**Title**

Table 3.1

Functional Requirements Specification

Table 3.2

Non-Functional Requirements Specification

Table 5.1

RBAC Permissions Matrix

Table 7.1

Test Results Summary

# **CHAPTER 1: INTRODUCTION**

## **1.1 Problem Statement**

Land administration in India continues to rely heavily on manual paper-based records. Physical Jamabandi registers are vulnerable to loss, tampering, and transcription errors. Revenue calculations require manual cross-referencing of land-use type, area, and circle rate — a process that introduces significant human error. Citizens have no direct, transparent access to their land records without visiting a government office in person.

The absence of a centralized, spatially-enabled digital system means that land-related disputes are difficult to resolve, revenue collection is inefficient, and there is no mechanism for citizens to verify their property records independently. The existing workflows are opaque, time-consuming, and prone to corruption at various administrative levels.

Furthermore, the manual system lacks integration between survey departments, revenue offices, and registration authorities. Cadastral maps are maintained in disparate formats, and there is no unified geospatial database that allows for efficient querying, visualization, or analysis of land parcel data. These systemic issues result in delayed mutation processing, inaccurate revenue assessments, and a general lack of trust in the land administration framework.

## **1.2 Proposed System**

The proposed Land Information Management System (LIMS) addresses the aforementioned challenges through a comprehensive, web-based GIS platform. The key components of the proposed system are:

• An interactive OpenStreetMap-based GIS viewer for spatial land parcel lookup

• Automated revenue assessment using statutory land-use multipliers

• A secure multi-tier administrative dashboard for record management

• One-click generation of PDF Property Cards (Khasra Patta) with embedded QR codes

• Dual deployment: cloud (Render) and standalone Windows executable (PyWebView)

The system leverages MongoDB for flexible document-based storage of land records, Shapely for geospatial computations such as area calculation and containment checks, and a Flask-based REST API for seamless communication between the frontend and backend components.

## **1.3 Objectives**

The primary objectives of this project are as follows:

**1\.** To assign and validate Unique Land Parcel Identification Numbers (ULPINs) for every registered land parcel in the database, ensuring unambiguous identification across all administrative layers.

**2\.** To implement a Role-Based Access Control (RBAC) framework with four distinct tiers (Public, Revenue Officer, Circle Officer, Admin), ensuring that sensitive operations are restricted to authorized personnel only.

**3\.** To automate land revenue calculation by integrating land-use classification data, circle rates, and standard area measurement conversions, thereby minimizing manual computation errors.

**4\.** To provide a soft-delete mechanism for land records that preserves data integrity during ownership mutations, allowing reversible deletion and comprehensive audit trail maintenance.

**5\.** To generate QR-code-embedded PDF Property Cards (Khasra Patta) that serve as verifiable, portable, and tamper-evident documents for citizens and government officials alike.

# **CHAPTER 2: SDLC MODEL**

## **2.1 Software Development Life Cycle**

The Software Development Life Cycle (SDLC) provides a structured framework for planning, creating, testing, and deploying an information system. For the LIMS project, the Iterative and Incremental model was selected as the most appropriate SDLC approach. This model divides the development process into smaller, manageable iterations, each delivering a functional increment of the system.

The iterative approach was chosen because it accommodates evolving requirements typical of government information systems, allows for early and continuous feedback from stakeholders, and enables incremental testing and validation at each phase. This is particularly important for a land management system where regulatory requirements may change and user feedback from different administrative tiers must be incorporated progressively.

## **2.2 Iterative and Incremental Model**

The Iterative and Incremental SDLC model follows a cyclical pattern where each iteration passes through the core phases of requirements gathering, design, implementation, testing, and review. Unlike the waterfall model, each iteration produces a working increment that can be demonstrated to stakeholders and evaluated against project requirements.

The LIMS project was organized into four major iterations, each corresponding to a critical functional module of the system. This approach ensured that core functionalities were delivered early and could be refined based on user feedback.

![]()

_Figure 2.1: Iterative and Incremental SDLC Model_

## **2.3 SDLC Phases**

The key phases of the SDLC adopted for this project include Requirements Analysis, System Design, Implementation, Testing, and Deployment. Each phase has defined deliverables and review gates that ensure quality and traceability throughout the development lifecycle.

![]()

_Figure 2.2: SDLC Phases Overview_

## **2.4 Iteration Plan**

The four iterations planned for the LIMS project are structured as follows:

**1\.** Iteration 1 - Foundation: Database schema design, user authentication with CAPTCHA, RBAC middleware, and basic GIS viewer integration with OpenStreetMap.

**2\.** Iteration 2 - Core Records: Land record CRUD operations, point-in-polygon spatial queries, geodesic area computation, and revenue calculation engine with land-use multipliers.

**3\.** Iteration 3 - Documents & Export: PDF Property Card generation with QR codes, Excel export of land records, ownership mutation workflow with soft-delete, and audit logging.

**4\.** Iteration 4 - Deployment & Polish: Cloud deployment on Render, PyInstaller packaging for standalone Windows executable, comprehensive testing, and user manual documentation.

# **CHAPTER 3: REQUIREMENTS ANALYSIS**

## **3.1 Functional Requirements**

Functional requirements define the specific behaviors and functions that the LIMS system must implement. These requirements were derived from an analysis of existing manual workflows in land revenue offices, stakeholder interviews with revenue officers and circle officers, and a study of the Digital India Land Records Modernization Programme (DILRMP) guidelines.

The following table enumerates the core functional requirements identified for the LIMS system:

**Req ID**

**Requirement Description**

**Priority**

FR-1

CAPTCHA challenge on login page to prevent automated brute-force attacks

High

FR-2

Point-in-Polygon spatial query to identify land parcels from map clicks

High

FR-3

ULPIN generation and validation for unique land parcel identification

High

FR-4

Ownership mutation processing with digital approval workflow

High

FR-5

Soft-delete mechanism for land records with audit trail

Medium

FR-6

PDF Property Card (Khasra Patta) generation with embedded QR codes

High

FR-7

Excel export of filtered land records with configurable columns

Medium

FR-8

Reverse geocoding to convert geographic coordinates to administrative addresses

Medium

## **3.2 Non-Functional Requirements**

Non-functional requirements specify the quality attributes, constraints, and performance benchmarks that the system must satisfy. These requirements ensure that the LIMS system is secure, reliable, and maintainable in a production environment.

The non-functional requirements identified for this project are summarized in the table below:

**Req ID**

**Requirement Description**

**Category**

NFR-1

PBKDF2-HMAC-SHA256 with 200,000 iterations for password hashing

Security

NFR-2

GeoJSON storage format for all geospatial polygon data

Data

NFR-3

TLS 1.3 encryption for all client-server communications

Security

NFR-4

Session-based authentication with 30-minute idle timeout

Security

NFR-5

Geofencing validation for all spatial polygon submissions

Data Integrity

NFR-6

Cache-Control headers with no-store directive for sensitive pages

Performance

# **CHAPTER 4: SYSTEM DESIGN**

## **4.1 Context-Level Data Flow Diagram**

The context-level DFD provides a high-level view of the LIMS system, showing it as a single process that interacts with external entities. The primary external entities include the Citizen (public user), Revenue Officer, Circle Officer, System Administrator, and the MongoDB database. The context diagram illustrates the flow of information between these entities and the system boundary.

![]()

_Figure 4.1: Context-Level Data Flow Diagram_

## **4.2 Level-1 DFD**

The Level-1 DFD decomposes the LIMS system into five major processes: Authentication, GIS Processing, Record Management, Document Generation, and Administration. Each process represents a functional subsystem with its own internal data stores and information flows.

![]()

_Figure 4.2: Level-1 DFD_

## **4.3 Level-2 DFD for Mutation Processing**

The Level-2 DFD provides a detailed decomposition of the mutation processing subsystem. It shows the step-by-step flow of data during an ownership transfer, including record lookup, verification, approval routing, database update, and audit logging. This diagram highlights the validation checkpoints and approval gates that ensure data integrity during mutations.

![]()

_Figure 4.3: Level-2 DFD for Mutation Processing_

## **4.4 Entity-Relationship Diagram**

The ER diagram models the core data entities in the LIMS database and their relationships. The primary entities include User, LandRecord, MutationRequest, AuditLog, and Session. The User entity maintains role-based attributes for RBAC enforcement. The LandRecord entity stores geospatial data in GeoJSON format along with ownership and revenue details.

![]()

_Figure 4.4: Entity-Relationship Diagram_

## **4.5 Use Case Diagram**

The use case diagram captures the functional interactions between the four actor types (Public, Revenue Officer, Circle Officer, Admin) and the system. Key use cases include spatial parcel lookup, land record creation and modification, mutation approval, PDF generation, user management, and system configuration. Each use case is associated with specific RBAC permission requirements.

![]()

_Figure 4.5: Use Case Diagram_

## **4.6 Class Diagram**

The class diagram illustrates the static structure of the LIMS application, showing the key classes, their attributes, methods, and relationships. The diagram includes classes for the Flask application, database models, GIS processor, PDF generator, security module, and API route handlers. Inheritance and composition relationships are used to model the object-oriented design of the system.

![]()

_Figure 4.6: Class Diagram_

## **4.7 Object Diagram**

The object diagram shows a snapshot of the LIMS system at runtime, depicting specific object instances and their relationships. This diagram provides a concrete example of how LandRecord, User, and MutationRequest objects interact during a typical ownership transfer operation.

![]()

_Figure 4.7: Object Diagram_

## **4.8 Sequence Diagram**

The sequence diagram models the dynamic interaction between system components during a complete land record mutation flow. It traces the sequence of messages exchanged between the user interface, Flask API, authentication middleware, database layer, and PDF generation module from the initiation of a mutation request to its final approval and document generation.

![]()

_Figure 4.8: Sequence Diagram_

## **4.9 Activity Diagram - Ownership Mutation Workflow**

The activity diagram details the complete workflow for processing an ownership mutation request. It covers all decision points, including role verification, data validation, approval routing, database updates, and notification triggers. The diagram uses swimlanes to distinguish between actions performed by the applicant, the revenue officer, and the system.

![]()

_Figure 4.9: Activity Diagram - Ownership Mutation Workflow_

## **4.10 Activity Diagram - User Login Flow**

The activity diagram for the user login flow illustrates the authentication process from CAPTCHA generation and validation through credential verification, session creation, and role-based redirection. It includes error handling paths for invalid CAPTCHA responses, incorrect credentials, and account lockout scenarios.

![]()

_Figure 4.10: Activity Diagram - User Login Flow_

## **4.11 PDF Property Card Generation Flow**

The PDF generation flow diagram shows the end-to-end process of creating a Property Card (Khasra Patta) from a land record. It includes data retrieval from the database, QR code generation, PDF layout construction using fpdf2, and the final output delivery to the user. The diagram also illustrates how GeoJSON boundary data is rendered as a simplified polygon sketch within the PDF document.

![]()

_Figure 4.11: PDF Property Card Generation Flow_

# **CHAPTER 5: SECURITY ARCHITECTURE**

## **5.1 Role-Based Access Control (RBAC)**

The LIMS system implements a four-tier Role-Based Access Control framework that governs all access to system resources and operations. The four roles are: Public (unauthenticated or read-only users), Revenue Officer (field-level data entry and mutation processing), Circle Officer (supervisory approval and audit review), and System Administrator (full system management privileges).

Each API endpoint in the system is decorated with role-checking decorators that verify the authenticated user's role against the required permission level. Unauthorized access attempts are logged and result in HTTP 403 Forbidden responses.

The following table presents the complete RBAC permissions matrix showing which operations are available to each role:

**Permission**

**Public**

**Revenue Officer**

**Circle Officer**

**Admin**

View Map / Search Parcels

✓

✓

✓

✓

View Record Details

✓

✓

✓

✓

Create Land Record

✗

✓

✓

✓

Edit Land Record

✗

✓

✗

✓

Delete Land Record (Soft)

✗

✗

✗

✓

Approve Mutations

✗

✓

✓

✓

Generate PDF Cards

✗

✓

✓

✓

Export to Excel

✗

✓

✓

✓

Manage Users

✗

✗

✗

✓

View Audit Logs

✗

✗

✓

✓

System Configuration

✗

✗

✗

✓

![]()

_Figure 5.1: RBAC Permission Tiers_

## **5.2 CAPTCHA Implementation**

To protect against automated brute-force attacks on the login endpoint, the LIMS system generates and validates CAPTCHA challenges using the Pillow library. Each login attempt requires the user to correctly identify a distorted text image rendered with random font rotation, noise lines, and color variations. The CAPTCHA solution is stored in the server-side session and validated before credential checking.

![]()

_Figure 5.2: CAPTCHA Generation and Validation Lifecycle_

## **5.3 Password Security**

All user passwords are hashed using the PBKDF2-HMAC-SHA256 algorithm with 200,000 iterations and a cryptographically random 32-byte salt. This approach aligns with NIST SP 800-132 recommendations for password-based key derivation. The hashing process ensures that even in the event of a database breach, plaintext passwords cannot be recovered from the stored hashes.

![]()

_Figure 5.3: Password Hashing and Verification Flow_

## **5.4 Session Management**

The LIMS system uses server-side sessions stored in MongoDB with configurable expiration times. Session tokens are transmitted via secure, HTTP-only cookies to prevent cross-site scripting (XSS) token theft. The session middleware automatically invalidates sessions after 30 minutes of inactivity and supports explicit logout functionality that immediately revokes the session token.

# **CHAPTER 6: IMPLEMENTATION**

## **6.1 Technology Stack**

The LIMS system is built using a carefully selected technology stack that prioritizes reliability, geospatial processing capability, and ease of deployment. The following table presents the complete software technology stack used in the project:

**Technology**

**Version / Details**

**Purpose**

Flask

3.0.0

Web framework for REST API and server-side rendering

PyMongo

4.6.1

MongoDB Python driver for database operations

Shapely

2.0.2

Geospatial geometry operations (area, containment)

fpdf2

2.7.6

PDF generation for Property Cards

OpenPyXL + Pandas

3.1.2 / 2.1.4

Excel export with data formatting

qrcode

7.4.2

QR code generation for Property Card embedding

Tailwind CSS

3.4.1

Utility-first CSS framework for frontend styling

Leaflet.js

1.9.4

Interactive map rendering with OpenStreetMap tiles

Gunicorn

21.2.0

Production WSGI HTTP server

PyWebView

4.4.1

Lightweight native window wrapper for desktop mode

PyInstaller + Inno Setup

6.3.0 / 6.2.1

Executable packaging and Windows installer

## **6.2 Database Schema - Users Collection**

The users collection stores authentication and profile information for all system users. The schema is designed to support the RBAC framework with a dedicated role field that maps to one of four permission tiers.

**Field**

**Type**

**Description**

\_id

ObjectId

Auto-generated unique identifier

username

String

Unique login username

password\_hash

String

PBKDF2-HMAC-SHA256 hashed password

role

String

RBAC role: public, revenue\_officer, circle\_officer, admin

full\_name

String

Full name of the user

email

String

Email address for communication

created\_at

DateTime

Account creation timestamp

is\_active

Boolean

Account active status flag

## **6.3 Database Schema - Land Records Collection**

The land\_records collection is the central data store of the LIMS system. Each document represents a single land parcel and includes ownership details, geospatial geometry in GeoJSON format, revenue computation fields, and soft-delete metadata.

**Field**

**Type**

**Description**

\_id

ObjectId

Auto-generated unique identifier

ulpin

String

Unique Land Parcel Identification Number

owner\_name

String

Current owner full name

owner\_father

String

Father name of the owner

village

String

Village name

circle

String

Revenue circle name

district

String

District name

land\_use

String

Classification: commercial, residential, agricultural, etc.

area\_acres

Float

Total area in acres

geometry

GeoJSON

Polygon boundary coordinates

circle\_rate

Float

Government circle rate per unit area

revenue

Float

Computed annual land revenue

is\_deleted

Boolean

Soft-delete flag

created\_at

DateTime

Record creation timestamp

updated\_at

DateTime

Last modification timestamp

## **6.4 Database Schema - Audit Log Collection**

The audit\_log collection maintains an immutable record of all significant operations performed on the system. Every create, update, delete, restore, and mutation action is logged with the performing user, timestamp, and relevant details.

**Field**

**Type**

**Description**

\_id

ObjectId

Auto-generated unique identifier

record\_id

ObjectId

Reference to the affected land record

action

String

Operation type: create, update, delete, restore, mutation

performed\_by

String

Username of the user who performed the action

timestamp

DateTime

Exact time of the action

details

Object

Additional metadata about the action

## **6.5 Revenue Calculation Engine**

The revenue calculation engine computes annual land revenue by multiplying the land area by the applicable circle rate and then applying a land-use multiplier. The land-use multiplier reflects the differential revenue rates for different categories of land use, as mandated by government policy. The following tables define the multiplier values and unit conversion factors used in the computation:

**Land-Use Category**

**Revenue Multiplier**

Commercial

2.5

Industrial

1.8

Residential

1.5

Government

1.2

Agricultural

1.0

Forest

0.8

Wasteland

0.5

**Unit**

**Conversion Factor (1 sq. meter)**

Acre

2.47105

Bigha (Assam)

7.4752

Lecha (Assam)

747.52

## **6.6 API Documentation**

The LIMS backend exposes a RESTful API built with Flask. All endpoints return JSON responses and follow standard HTTP status codes. The following table documents the complete API surface of the system:

**Endpoint**

**Method**

**Description**

**Auth Required**

/api/auth/login

POST

User login with CAPTCHA verification

No

/api/auth/logout

POST

Terminate user session

Yes

/api/records

GET

List land records with filtering

Yes

/api/records

POST

Create a new land record

Revenue+

/api/records/<id>

PUT

Update an existing land record

Revenue+

/api/records/<id>

DELETE

Soft-delete a land record

Admin

/api/gis/point-query

POST

Point-in-polygon spatial query

Yes

/api/gis/reverse-geocode

GET

Convert coordinates to address

Yes

/api/mutations

POST

Submit ownership mutation request

Revenue+

/api/mutations/<id>/approve

PUT

Approve a mutation request

Officer+

/api/docs/pdf/<id>

GET

Generate PDF Property Card

Yes

/api/docs/excel

GET

Export filtered records to Excel

Revenue+

/api/dashboard/stats

GET

Dashboard summary statistics

Officer+

/api/users

GET

List all system users

Admin

/api/audit

GET

View audit log entries

Officer+

## **6.7 CAPTCHA Generation Module**

The CAPTCHA generation module, located in core/security.py, creates randomized text challenges using the Pillow image processing library. The generated CAPTCHA image includes rotated characters, random color noise, and interference lines to resist automated optical character recognition. The following code snippet shows the implementation:

from PIL import Image, ImageDraw, ImageFont

import random, string, io, base64

def generate\_captcha(length=5):

    width, height = 160, 50

    image = Image.new('RGB', (width, height), color=(240, 240, 240))

    draw = ImageDraw.Draw(image)

    chars = string.ascii\_uppercase + string.digits

    captcha\_text = ''.join(random.choices(chars, k=length))

    for i, ch in enumerate(captcha\_text):

        x = 10 + i \* 28

        y = random.randint(5, 15)

        color = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))

        draw.text((x, y), ch, fill=color, font=ImageFont.load\_default())

    for \_ in range(5):

        x1 = random.randint(0, width)

        y1 = random.randint(0, height)

        x2 = random.randint(0, width)

        y2 = random.randint(0, height)

        draw.line(\[(x1, y1), (x2, y2)\], fill=(200, 200, 200), width=1)

    buf = io.BytesIO()

    image.save(buf, format='PNG')

    return captcha\_text, base64.b64encode(buf.getvalue()).decode()

## **6.8 Geodesic Area Computation**

The GIS processor module (gis\_processor.py) implements geodesic area calculation using the Shoelace formula adapted for spherical geometry. This provides accurate area measurements in square meters and acres for land parcels defined by geographic coordinates. The module also includes point-in-polygon containment checking using Shapely:

from shapely.geometry import Polygon, Point, shape

from geopy.distance import geodesic

def compute\_geodesic\_area(coordinates):

    polygon = Polygon(coordinates)

    if not polygon.is\_valid:

        polygon = polygon.buffer(0)

    coords = list(polygon.exterior.coords)

    total = 0.0

    n = len(coords) - 1

    for i in range(n):

        lat1, lon1 = coords\[i\]

        lat2, lon2 = coords\[i + 1\]

        total += (lon2 - lon1) \* (2 + math.sin(math.radians(lat1))

                  + math.sin(math.radians(lat2)))

    area\_sqm = abs(total \* 6378137.0 \* 6378137.0 / 2.0)

    area\_acres = area\_sqm \* 0.000247105

    return round(area\_sqm, 2), round(area\_acres, 4)

def point\_in\_polygon(point, polygon\_coords):

    pt = Point(point\['lng'\], point\['lat'\])

    poly = Polygon(polygon\_coords)

    return poly.contains(pt) or poly.touches(pt)

## **6.9 Ownership Mutation Processing**

The mutation processing endpoint in routes/records.py handles the submission of ownership transfer requests. The endpoint validates the existence of the source record, creates a mutation document with pending status, and logs the action in the audit trail. The following code snippet illustrates the implementation:

@records\_bp.route('/mutations', methods=\['POST'\])

@role\_required('revenue\_officer')

def submit\_mutation():

    data = request.get\_json()

    record\_id = data.get('record\_id')

    new\_owner = data.get('new\_owner\_details')

    record = db.land\_records.find\_one({'\_id': ObjectId(record\_id)})

    if not record or record.get('is\_deleted'):

        return jsonify({'error': 'Record not found'}), 404

    mutation = {

        'record\_id': ObjectId(record\_id),

        'previous\_owner': record\['owner\_name'\],

        'new\_owner': new\_owner,

        'status': 'pending',

        'submitted\_by': session\['user'\],

        'submitted\_at': datetime.utcnow(),

        'approved\_by': None,

        'approved\_at': None

    }

    result = db.mutations.insert\_one(mutation)

    db.audit\_log.insert\_one({

        'action': 'mutation\_submit',

        'record\_id': ObjectId(record\_id),

        'performed\_by': session\['user'\],

        'timestamp': datetime.utcnow()

    })

    return jsonify({'mutation\_id': str(result.inserted\_id)}), 201

# **CHAPTER 7: TESTING**

## **7.1 Testing Strategy**

The LIMS system was tested using a combination of unit tests, integration tests, and role-based permission tests. The testing framework used is pytest with the Flask test client. Each test module targets a specific subsystem and verifies both positive and negative scenarios. Tests were executed against a dedicated test database to avoid contamination of production data.

## **7.2 Test Results**

The following table presents the comprehensive test results for all test scripts executed during the verification phase of the project. All tests passed successfully within acceptable time limits:

**Test Script**

**Test Description**

**Result**

**Duration**

test\_logins.py

Verify login with valid credentials across all roles

PASS

2.3s

test\_logins.py

Verify CAPTCHA rejection on incorrect input

PASS

1.8s

robust\_role\_test.py

Verify RBAC enforcement for all 11 permissions across 4 roles

PASS

4.1s

test\_record\_soft\_delete.py

Verify soft-delete sets is\_deleted flag and hides from queries

PASS

1.5s

test\_record\_soft\_delete.py

Verify deleted records remain in database

PASS

0.9s

test\_restore\_flow.py

Verify admin restore of soft-deleted record

PASS

1.2s

test\_restore\_flow.py

Verify non-admin restore attempt is rejected

PASS

0.8s

check\_users\_roles.py

Verify all user accounts have correct role assignments

PASS

0.6s

test\_gis\_query.py

Verify point-in-polygon returns correct parcel

PASS

2.7s

test\_pdf\_generation.py

Verify PDF card generation with QR code

PASS

3.4s

## **7.3 Soft-Delete Test Verification**

The soft-delete mechanism is a critical feature of the LIMS system. The following test code snippet demonstrates how the soft-delete functionality is verified, including checks for record hiding from normal queries and database persistence:

def test\_soft\_delete(client, admin\_headers, sample\_record):

    response = client.delete(

        f'/api/records/{sample\_record}',

        headers=admin\_headers

    )

    assert response.status\_code == 200

    assert response.json\['message'\] == 'Record soft-deleted'

    # Verify record is hidden from normal queries

    response = client.get('/api/records', headers=admin\_headers)

    assert response.status\_code == 200

    ids = \[r\['\_id'\] for r in response.json\['records'\]\]

    assert sample\_record not in ids

    # Verify record still exists in database

    from app import db

    record = db.land\_records.find\_one(

        {'\_id': ObjectId(sample\_record)},

        {'is\_deleted': 1}

    )

    assert record is not None

    assert record\['is\_deleted'\] is True

# **CHAPTER 8: DEPLOYMENT**

## **8.1 Cloud Deployment on Render**

The LIMS system is deployed on Render, a cloud platform that provides fully managed web services. The deployment configuration is defined in a render.yaml file that specifies the web service, build commands, start command, environment variables, and MongoDB Atlas connection string. The Render platform handles automatic SSL certificate provisioning, continuous deployment from the GitHub repository, and horizontal scaling.

The render.yaml configuration specifies the following key parameters: the Python version (3.11.x), the build command (pip install -r requirements.txt), the start command (gunicorn app:app), and environment variables for the MongoDB connection URI, session secret, and CAPTCHA configuration. Health checks are configured on the /api/health endpoint to ensure service availability.

![]()

_Figure 8.1: Cloud Deployment Architecture on Render_

## **8.2 Standalone Executable with PyInstaller**

For offline deployment in government offices with limited internet connectivity, the LIMS system is packaged as a standalone Windows executable using PyInstaller. The IndiaLIMS.spec file defines the build configuration, including the entry point script, data files to bundle (templates, static assets), and hidden imports. The resulting executable is distributed with an Inno Setup installer that creates desktop shortcuts, Start Menu entries, and file associations.

The PyInstaller build process creates a single-directory bundle containing the Python interpreter, all dependencies, and the application code. The executable launches a PyWebView window that renders the Flask application in a native browser component, providing a desktop application experience without requiring a web browser or internet connection.

The Inno Setup installer (inno\_setup.iss) provides a professional installation wizard with license agreement display, custom directory selection, and automatic creation of desktop shortcuts. The installer also includes an uninstaller for clean removal of the application.

![]()

_Figure 8.2: PyInstaller Executable Packaging Workflow_

# **CHAPTER 9: USER MANUAL**

## **9.1 Public Viewer Workflow**

The public viewer interface allows any citizen to search for and view land records without authentication. The following steps describe the typical usage workflow:

**1\.** Open the LIMS application URL in a web browser (or launch the desktop application).

**2\.** The interactive GIS map loads automatically, centered on the default geographic region.

**3\.** Use the search bar to enter a village name, ULPIN, or owner name to locate a specific parcel.

**4\.** Alternatively, zoom and pan on the map and click on any land parcel boundary to select it.

**5\.** A popup displays the parcel details including owner name, area, land-use type, and revenue amount.

**6\.** Click the "View Full Record" button to see the complete record details.

**7\.** To generate a PDF Property Card, click the "Download PDF" button (login may be required).

## **9.2 Revenue Officer Workflow**

Revenue officers have elevated privileges that allow them to create, modify, and manage land records. The following steps outline the standard operating procedure:

**1\.** Log in to the system using your assigned username and password.

**2\.** Enter the CAPTCHA text displayed on the login page and click "Login."

**3\.** Upon successful authentication, the administrative dashboard loads with summary statistics.

**4\.** To create a new land record, click "New Record" and fill in the required fields: owner details, village, circle, district, land-use classification, and area.

**5\.** Draw the parcel boundary on the GIS map using the polygon drawing tool.

**6\.** The system automatically computes the geodesic area and calculates the annual revenue.

**7\.** Click "Save Record" to submit the record to the database.

**8\.** To process an ownership mutation, navigate to the record, click "Initiate Mutation," and enter the new owner details.

**9\.** The mutation request is submitted for approval and appears in the pending mutations queue.

**10\.** Export records to Excel by applying filters and clicking "Export to Excel."

## **9.3 System Administrator Workflow**

System administrators have full access to all system functions including user management, audit log review, and system configuration. The following steps describe the administrative workflow:

**1\.** Log in with admin credentials and complete the CAPTCHA challenge.

**2\.** The admin dashboard displays system-wide statistics including total records, users, pending mutations, and recent activity.

**3\.** To manage users, navigate to "User Management" in the admin panel.

**4\.** Create new user accounts by specifying username, password, full name, email, and role assignment.

**5\.** Edit existing user accounts to change roles, reset passwords, or deactivate accounts.

**6\.** Review the audit log by navigating to "Audit Trail" and applying date, user, and action filters.

**7\.** To restore a soft-deleted record, search for the record using the "Include Deleted" filter option and click "Restore."

**8\.** Access system configuration to modify CAPTCHA settings, session timeout values, and revenue multiplier rates.

**9\.** Monitor system health through the dashboard and review server logs for any anomalies.

# **CHAPTER 10: OUTPUT**

## **10.1 System Screenshots**

This section presents representative screenshots of the LIMS application captured during runtime. These screenshots illustrate the key user interfaces and demonstrate the functionality implemented in the system.

The following screenshot shows the system login interface with the CAPTCHA challenge displayed below the login form. The interface uses a clean, responsive design built with Tailwind CSS that adapts to both desktop and mobile screen sizes.

_\[ Screenshot Placeholder: Login Landscape \]_

_Figure 10.1: System Login Interface_

The GIS Interactive Viewer screenshot demonstrates the map-based parcel search interface. Users can zoom, pan, and click on parcel boundaries to retrieve detailed land record information. The sidebar panel displays the filtered results list and the selected parcel details.

_\[ Screenshot Placeholder: GIS Interactive Viewer \]_

_Figure 10.2: GIS Interactive Land Parcel Viewer_

## **10.2 Generated Documents**

The PDF Property Card is the primary document output of the LIMS system. Each Property Card includes the owner details, parcel information, revenue assessment, a simplified boundary sketch, and a QR code that links to the online record for verification.

_\[ Screenshot Placeholder: Sample Property Card PDF \]_

_Figure 10.3: Sample Property Card PDF Output_

# **CHAPTER 11: CONCLUSION**

## **11.1 Conclusion**

The Land Information Management System (LIMS) successfully demonstrates the application of modern web technologies and geospatial computing to the domain of land administration. The system addresses the critical challenges of manual record-keeping, opaque revenue calculations, and lack of citizen access by providing an integrated platform for spatial land parcel management, automated revenue assessment, and digital document generation.

The implementation of a four-tier RBAC framework ensures that sensitive operations are restricted to authorized personnel, while the public interface provides transparent access to land records for citizens. The use of industry-standard security practices, including PBKDF2 password hashing, CAPTCHA-based login protection, and TLS encryption, ensures that the system meets the security requirements expected of a government information system.

The dual deployment strategy, supporting both cloud-hosted and standalone Windows executable modes, ensures that the system can be deployed in diverse operational environments, from well-connected urban offices to remote locations with limited internet infrastructure. The comprehensive test suite, with all tests passing, validates the correctness and reliability of the implemented features.

## **11.2 Limitations**

Despite the comprehensive feature set, the current implementation has certain limitations that should be acknowledged:

• API Dependency: The system relies on external APIs for reverse geocoding (Nominatim) and map tile rendering (OpenStreetMap). Service unavailability of these APIs would affect GIS functionality.

• Single Instance Deployment: The current architecture is designed for single-server deployment and does not include horizontal scaling or load balancing for high-traffic scenarios.

• Manual Geometry Creation: Parcel boundaries must be drawn manually on the map interface. There is no support for bulk import of cadastral data from existing survey databases or shapefiles.

## **11.3 Future Work**

The following enhancements are planned for future versions of the LIMS system:

• Blockchain Integration: Implementation of a distributed ledger for immutable land transaction records, providing an additional layer of tamper-proof auditability.

• AI-Powered Encroachment Detection: Integration of satellite imagery analysis with machine learning models to automatically detect and flag unauthorized land encroachments.

• Aadhaar eKYC Integration: Linking land records with the Aadhaar biometric identity system for streamlined owner verification and digital signature-based mutation approval.

• Mobile Application: Development of a native Android and iOS application for field surveyors to capture parcel data and process mutations directly from the field.

• Multi-Language Support: Addition of Assamese, Bengali, and Hindi language interfaces to improve accessibility for diverse user populations in the state.

**REFERENCES**

\[1\] Chamberlain, R. G., & Duquette, W. H. (2007). _Some Algorithms for Polygons on a Sphere._ NASA Jet Propulsion Laboratory. NTRS Report ID: 20210005701. https://ntrs.nasa.gov/citations/20210005701

\[2\] Government of Assam (2022). "Assam Integrated Land Records Management System (ILRMS)." Revenue and Disaster Management Department.

\[3\] Ministry of Rural Development, Government of India (2008). "Digital India Land Records Modernization Programme (DILRMP)." National Land Records Modernisation Programme Guidelines.

\[4\] The Assam Land and Revenue Regulation, 1886. Government of Assam. Available at: http://assamlegislative.gov.in/acts/assam-land-and-revenue-regulation-1886

\[5\] The Assam Land Revenue Act, 1936. Government of Assam. Available at: http://assamlegislative.gov.in/acts/assam-land-revenue-act-1936

\[6\] Butler, H., Daly, M., Doyle, A., Gillies, S., Schaub, T., and C. Schmid (2016). "The GeoJSON Format." RFC 7946. Internet Engineering Task Force. https://tools.ietf.org/html/rfc7946

\[7\] Barker, E. (2010). "Recommendation for Password-Based Key Derivation: Part 1: Storage and Application of Password-Based Key Derivation Functions (PBKDF2)." NIST SP 800-132. National Institute of Standards and Technology.

\[8\] ISO/IEC 18004:2015. "Information Technology - Automatic Identification and Data Capture Techniques - QR Code 2005 Bar Code Symbology Specification." International Organization for Standardization.

\[9\] Grinberg, M. (2018). "Flask Web Development: Developing Web Applications with Python." 2nd Edition. O'Reilly Media.

\[10\] MongoDB Inc. (2024). "MongoDB Atlas Documentation." https://www.mongodb.com/docs/atlas/

\[11\] Agafonkin, V. (2023). "Leaflet.js - An Open-Source JavaScript Library for Mobile-Friendly Interactive Maps." https://leafletjs.com/

\[12\] DataMeet (2023). "Open Data Community for India." https://datameet.org/

\[13\] OpenStreetMap Contributors (2024). "OpenStreetMap." https://www.openstreetmap.org/

\[14\] Nominatim Contributors (2024). "Nominatim - OpenStreetMap Geocoding Service." https://nominatim.org/