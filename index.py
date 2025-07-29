import pandas as pd
import os

def handler(request):
    os.makedirs("daily_reports", exist_ok=True)
    os.makedirs("recruitment_employee", exist_ok=True)

    pattama_data = {
        "Date": ["15-Jan-2025", "15-Jan-2025"],
        "Candidate Name": ["Mr.A", "Mr.B"],
        "Role": ["Data Analyst", "Web Developer"],
        "Interview": ["Yes", "Yes"],
        "Status": ["Pass", "Fail"],
        "Remark": ["", ""]
    }
    pd.DataFrame(pattama_data).to_excel("daily_reports/Daily_report_Pattama.xlsx", index=False)

    raewwadee_data = {
        "Date": ["15-Jan-2025", "15-Jan-2025"],
        "Candidate Name": ["Mr.C", "Mr.D"],
        "Role": ["Software Tester", "Project Coordinator"],
        "Interview": ["Yes", "Yes"],
        "Status": ["Fail", "Pass"],
        "Remark": ["", ""]
    }
    pd.DataFrame(raewwadee_data).to_excel("daily_reports/Daily_report_Raewwadee.xlsx", index=False)

    new_employee_data = {
        "Employee Name": ["Mr.A", "Mr.D"],
        "Join Date": ["3-Feb-2025", "17-Feb-2025"],
        "Role": ["Data Analyst", "Project Coordinator"],
        "DOB": ["01-01-2000", "01-12-2001"],
        "ID Card": ["1-1111-11111-11-1", "2-2222-2222-22-2"],
        "Remark": ["", ""]
    }
    pd.DataFrame(new_employee_data).to_excel("recruitment_employee/New_Employees.xlsx", index=False)

    pattama = pd.read_excel("daily_reports/Daily_report_Pattama.xlsx")
    raewwadee = pd.read_excel("daily_reports/Daily_report_Raewwadee.xlsx")
    new_employees = pd.read_excel("recruitment_employee/New_Employees.xlsx")

    pattama["Interviewer"] = "Pattama Sooksan"
    raewwadee["Interviewer"] = "Raewwadee Jaidee"

    all_interviews = pd.concat([pattama, raewwadee])

    result = pd.merge(
        new_employees,
        all_interviews[["Candidate Name", "Role", "Interviewer"]],
        left_on=["Employee Name", "Role"],
        right_on=["Candidate Name", "Role"],
        how="left"
    )

    final = result[["Employee Name", "Join Date", "Role", "Interviewer"]]
    final = final.dropna()
    final.to_excel("recruitment_employee/Employee_Dashboard.xlsx", index=False)

    return {
        "statusCode": 200,
        "headers": { "Content-Type": "application/json" },
        "body": "Dashboard created successfully!"
    }
