# AssetTrackerPro-with-DRF

**Technology I used:**
* Django - Python web framework
* Database- PostgreSQL

### Database Design EF diagram:

![](https://github.com/Ridowan-sajid/AssetTrackerPro-with-DRF/blob/master/images/drawSQL-assettrackerpro-export-2023-08-24.png)

### Task:

**You have been hired as a developer for a new project where,
You will write a Django app to track corporate assets such as phones, tablets, laptops 
and other gears handed out to employees.**

### GOALS

**The application might be used by several companies
Each company might add all or some of its employees
Each company and its staff might delegate one or more devices to employees for
a certain period of time
Each company should be able to see when a Device was checked out and returned
Each device should have a log of what condition it was handed out and returned**

### OverView

**The application is designed to facilitate the usage of various features by registered companies. The process begins with company registration, where a company is required to provide its official title and a confidential company_code. This company_code serves as the authentication credential for subsequent logins.
Upon successful registration, the company gains the ability to log in using the provided company_code. Subsequent interactions within the application are governed by this authentication mechanism.
Once logged in, a company is empowered to create and manage multiple user accounts, catering to the company's needs. This involves the creation, modification, deletion, and retrieval of user records stored in the application's database.
Furthermore, the company is granted the authority to assign gadgets to users, along with pertinent details about each gadget. Additionally, the company can establish specific timeframes during which a gadget is permitted to be used. This feature enables the company to monitor both the checkout and return times of gadgets, ensuring efficient management of resources.
The application architecture employs a model-centric approach, distinguishing companies from users. This differentiation is made to accurately reflect the distinction between these two entities. While the application possesses the capability to utilize Django's default user-based authentication, this design decision favors a clear separation between companies and users.
Authentication of companies is primarily session-based. Upon successful login, a session is initiated for the authenticated company. This session persists throughout the company's interaction with the application and is terminated upon logout, providing a secure and controlled environment for company-specific activities.
In terms of database management, PostgreSQL is chosen as the preferred database system. This decision is rooted in its suitability and reliability for larger-scale projects, ensuring robust data storage and retrieval capabilities.
Should you require any further clarification or assistance in the implementation of specific aspects of this application, please do not hesitate to inquire.**
