from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Updated input data model
class SalaryPredictionRequest(BaseModel):
    job_title: str

    experience: int


    country: str
    


# Add your salary data (for Software Engineer role only as example)
software_engineer_salary_by_country = {
  "USA": { "base": 80000, "average": 120000, "highest": 160000 },
  "India": { "base": 400000, "average": 800000, "highest": 2000000 },
  "Canada": { "base": 70000, "average": 95000, "highest": 150000 },
  "UK": { "base": 60000, "average": 85000, "highest": 140000 },
  "Germany": { "base": 55000, "average": 90000, "highest": 130000 },
  "China": { "base": 100000, "average": 200000, "highest": 350000 },
  "Japan": { "base": 4500000, "average": 6000000, "highest": 10000000 },
  "South Korea": { "base": 40000000, "average": 60000000, "highest": 90000000 },
  "Australia": { "base": 70000, "average": 95000, "highest": 140000 },
  "Singapore": { "base": 60000, "average": 100000, "highest": 150000 },
  "Sweden": { "base": 45000, "average": 75000, "highest": 110000 },
  "Netherlands": { "base": 50000, "average": 80000, "highest": 120000 },
  "Switzerland": { "base": 90000, "average": 130000, "highest": 180000 },
  "France": { "base": 45000, "average": 75000, "highest": 110000 },
  "Israel": { "base": 70000, "average": 100000, "highest": 150000 }
}

full_stack_developer_salary_by_country = {
  "USA": { "base": 90000, "average": 130000, "highest": 180000 },
  "India": { "base": 600000, "average": 1200000, "highest": 2500000 },
  "Canada": { "base": 75000, "average": 105000, "highest": 160000 },
  "UK": { "base": 60000, "average": 85000, "highest": 130000 },
  "Germany": { "base": 60000, "average": 95000, "highest": 140000 },
  "China": { "base": 100000, "average": 180000, "highest": 350000 },
  "Japan": { "base": 4500000, "average": 6500000, "highest": 10000000 },
  "South Korea": { "base": 40000000, "average": 70000000, "highest": 100000000 },
  "Australia": { "base": 80000, "average": 110000, "highest": 150000 },
  "Singapore": { "base": 70000, "average": 105000, "highest": 150000 },
  "Sweden": { "base": 55000, "average": 80000, "highest": 120000 },
  "Netherlands": { "base": 60000, "average": 90000, "highest": 140000 },
  "Switzerland": { "base": 100000, "average": 140000, "highest": 200000 },
  "France": { "base": 50000, "average": 75000, "highest": 120000 },
  "Israel": { "base": 75000, "average": 110000, "highest": 150000 }
}

frontend_developer_salary_by_country = {
  "USA": { "base": 70000, "average": 100000, "highest": 150000 },
  "India": { "base": 500000, "average": 1000000, "highest": 2000000 },
  "Canada": { "base": 60000, "average": 85000, "highest": 130000 },
  "UK": { "base": 50000, "average": 75000, "highest": 110000 },
  "Germany": { "base": 55000, "average": 80000, "highest": 120000 },
  "China": { "base": 80000, "average": 150000, "highest": 250000 },
  "Japan": { "base": 4000000, "average": 6000000, "highest": 9000000 },
  "South Korea": { "base": 35000000, "average": 60000000, "highest": 90000000 },
  "Australia": { "base": 70000, "average": 95000, "highest": 130000 },
  "Singapore": { "base": 65000, "average": 95000, "highest": 140000 },
  "Sweden": { "base": 45000, "average": 70000, "highest": 100000 },
  "Netherlands": { "base": 50000, "average": 75000, "highest": 110000 },
  "Switzerland": { "base": 90000, "average": 120000, "highest": 170000 },
  "France": { "base": 45000, "average": 70000, "highest": 100000 },
  "Israel": { "base": 70000, "average": 95000, "highest": 130000 }
}

backend_developer_salary_by_country = {
  "USA": { "base": 75000, "average": 110000, "highest": 160000 },
  "India": { "base": 600000, "average": 1200000, "highest": 2500000 },
  "Canada": { "base": 65000, "average": 90000, "highest": 130000 },
  "UK": { "base": 55000, "average": 80000, "highest": 120000 },
  "Germany": { "base": 60000, "average": 90000, "highest": 130000 },
  "China": { "base": 90000, "average": 180000, "highest": 300000 },
  "Japan": { "base": 4500000, "average": 7000000, "highest": 10000000 },
  "South Korea": { "base": 40000000, "average": 65000000, "highest": 95000000 },
  "Australia": { "base": 75000, "average": 105000, "highest": 145000 },
  "Singapore": { "base": 70000, "average": 100000, "highest": 150000 },
  "Sweden": { "base": 50000, "average": 75000, "highest": 110000 },
  "Netherlands": { "base": 55000, "average": 80000, "highest": 120000 },
  "Switzerland": { "base": 95000, "average": 130000, "highest": 180000 },
  "France": { "base": 50000, "average": 75000, "highest": 110000 },
  "Israel": { "base": 75000, "average": 105000, "highest": 145000 }
}

mobile_app_developer_salary_by_country = {
  "USA": { "base": 75000, "average": 115000, "highest": 160000 },
  "India": { "base": 500000, "average": 1000000, "highest": 2200000 },
  "Canada": { "base": 65000, "average": 90000, "highest": 130000 },
  "UK": { "base": 50000, "average": 80000, "highest": 120000 },
  "Germany": { "base": 55000, "average": 85000, "highest": 125000 },
  "China": { "base": 80000, "average": 160000, "highest": 280000 },
  "Japan": { "base": 4000000, "average": 6000000, "highest": 9500000 },
  "South Korea": { "base": 38000000, "average": 60000000, "highest": 90000000 },
  "Australia": { "base": 70000, "average": 100000, "highest": 140000 },
  "Singapore": { "base": 60000, "average": 95000, "highest": 135000 },
  "Sweden": { "base": 45000, "average": 70000, "highest": 105000 },
  "Netherlands": { "base": 50000, "average": 80000, "highest": 115000 },
  "Switzerland": { "base": 90000, "average": 125000, "highest": 170000 },
  "France": { "base": 45000, "average": 70000, "highest": 105000 },
  "Israel": { "base": 70000, "average": 100000, "highest": 145000 }
}

game_developer_salary_by_country = {
  "USA": { "base": 65000, "average": 100000, "highest": 150000 },
  "India": { "base": 400000, "average": 900000, "highest": 1800000 },
  "Canada": { "base": 60000, "average": 85000, "highest": 130000 },
  "UK": { "base": 45000, "average": 70000, "highest": 110000 },
  "Germany": { "base": 50000, "average": 80000, "highest": 120000 },
  "China": { "base": 70000, "average": 150000, "highest": 250000 },
  "Japan": { "base": 3500000, "average": 5500000, "highest": 8500000 },
  "South Korea": { "base": 35000000, "average": 55000000, "highest": 85000000 },
  "Australia": { "base": 60000, "average": 90000, "highest": 130000 },
  "Singapore": { "base": 50000, "average": 85000, "highest": 120000 },
  "Sweden": { "base": 40000, "average": 70000, "highest": 100000 },
  "Netherlands": { "base": 45000, "average": 75000, "highest": 110000 },
  "Switzerland": { "base": 80000, "average": 120000, "highest": 170000 },
  "France": { "base": 40000, "average": 70000, "highest": 100000 },
  "Israel": { "base": 60000, "average": 90000, "highest": 130000 }
}

embedded_system_developer_salary_by_country ={
  "USA": { "base": 75000, "average": 105000, "highest": 150000 },
  "India": { "base": 400000, "average": 900000, "highest": 1800000 },
  "Canada": { "base": 60000, "average": 85000, "highest": 130000 },
  "UK": { "base": 50000, "average": 80000, "highest": 120000 },
  "Germany": { "base": 55000, "average": 85000, "highest": 125000 },
  "China": { "base": 80000, "average": 160000, "highest": 300000 },
  "Japan": { "base": 4000000, "average": 6000000, "highest": 9500000 },
  "South Korea": { "base": 35000000, "average": 55000000, "highest": 85000000 },
  "Australia": { "base": 65000, "average": 90000, "highest": 130000 },
  "Singapore": { "base": 55000, "average": 85000, "highest": 120000 },
  "Sweden": { "base": 45000, "average": 75000, "highest": 110000 },
  "Netherlands": { "base": 50000, "average": 80000, "highest": 115000 },
  "Switzerland": { "base": 85000, "average": 125000, "highest": 175000 },
  "France": { "base": 45000, "average": 75000, "highest": 110000 },
  "Israel": { "base": 65000, "average": 95000, "highest": 140000 }
}

devops_engineer_salary_by_country ={
  "USA": { "base": 90000, "average": 125000, "highest": 170000 },
  "India": { "base": 500000, "average": 1000000, "highest": 2500000 },
  "Canada": { "base": 70000, "average": 100000, "highest": 150000 },
  "UK": { "base": 60000, "average": 90000, "highest": 135000 },
  "Germany": { "base": 60000, "average": 95000, "highest": 140000 },
  "China": { "base": 100000, "average": 220000, "highest": 400000 },
  "Japan": { "base": 5000000, "average": 7000000, "highest": 11000000 },
  "South Korea": { "base": 45000000, "average": 65000000, "highest": 95000000 },
  "Australia": { "base": 75000, "average": 105000, "highest": 150000 },
  "Singapore": { "base": 65000, "average": 100000, "highest": 140000 },
  "Sweden": { "base": 50000, "average": 80000, "highest": 120000 },
  "Netherlands": { "base": 55000, "average": 85000, "highest": 125000 },
  "Switzerland": { "base": 95000, "average": 135000, "highest": 185000 },
  "France": { "base": 50000, "average": 80000, "highest": 120000 },
  "Israel": { "base": 75000, "average": 105000, "highest": 150000 }
}

ai_engineer_salary_by_country = {
  "USA": { "base": 100000, "average": 135000, "highest": 180000 },
  "India": { "base": 600000, "average": 1200000, "highest": 2500000 },
  "Canada": { "base": 80000, "average": 110000, "highest": 160000 },
  "UK": { "base": 65000, "average": 95000, "highest": 140000 },
  "Germany": { "base": 65000, "average": 100000, "highest": 145000 },
  "China": { "base": 120000, "average": 240000, "highest": 420000 },
  "Japan": { "base": 5500000, "average": 7500000, "highest": 11500000 },
  "South Korea": { "base": 45000000, "average": 70000000, "highest": 100000000 },
  "Australia": { "base": 80000, "average": 115000, "highest": 160000 },
  "Singapore": { "base": 70000, "average": 110000, "highest": 160000 },
  "Sweden": { "base": 55000, "average": 85000, "highest": 125000 },
  "Netherlands": { "base": 60000, "average": 90000, "highest": 130000 },
  "Switzerland": { "base": 100000, "average": 140000, "highest": 190000 },
  "France": { "base": 50000, "average": 85000, "highest": 125000 },
  "Israel": { "base": 80000, "average": 110000, "highest": 160000 }
}

data_scientist_salary_by_country = {
  "USA": { "base": 90000, "average": 125000, "highest": 170000 },
  "India": { "base": 500000, "average": 1000000, "highest": 2500000 },
  "Canada": { "base": 75000, "average": 105000, "highest": 150000 },
  "UK": { "base": 60000, "average": 90000, "highest": 135000 },
  "Germany": { "base": 60000, "average": 95000, "highest": 140000 },
  "China": { "base": 110000, "average": 220000, "highest": 400000 },
  "Japan": { "base": 5000000, "average": 7500000, "highest": 11000000 },
  "South Korea": { "base": 42000000, "average": 65000000, "highest": 95000000 },
  "Australia": { "base": 75000, "average": 100000, "highest": 140000 },
  "Singapore": { "base": 65000, "average": 100000, "highest": 140000 },
  "Sweden": { "base": 50000, "average": 80000, "highest": 115000 },
  "Netherlands": { "base": 55000, "average": 85000, "highest": 125000 },
  "Switzerland": { "base": 95000, "average": 135000, "highest": 185000 },
  "France": { "base": 50000, "average": 80000, "highest": 115000 },
  "Israel": { "base": 75000, "average": 105000, "highest": 155000 }
}

data_analyst_salary_by_country = {
  "USA": { "base": 65000, "average": 85000, "highest": 120000 },
  "India": { "base": 350000, "average": 700000, "highest": 1500000 },
  "Canada": { "base": 60000, "average": 80000, "highest": 110000 },
  "UK": { "base": 45000, "average": 70000, "highest": 100000 },
  "Germany": { "base": 50000, "average": 75000, "highest": 100000 },
  "China": { "base": 80000, "average": 150000, "highest": 300000 },
  "Japan": { "base": 4000000, "average": 5500000, "highest": 9000000 },
  "South Korea": { "base": 35000000, "average": 50000000, "highest": 80000000 },
  "Australia": { "base": 60000, "average": 80000, "highest": 110000 },
  "Singapore": { "base": 55000, "average": 85000, "highest": 120000 },
  "Sweden": { "base": 40000, "average": 65000, "highest": 90000 },
  "Netherlands": { "base": 45000, "average": 70000, "highest": 95000 },
  "Switzerland": { "base": 75000, "average": 100000, "highest": 140000 },
  "France": { "base": 40000, "average": 65000, "highest": 90000 },
  "Israel": { "base": 60000, "average": 85000, "highest": 120000 }
}

machine_learning_engineer_salary_by_country = {
  "USA": { "base": 95000, "average": 125000, "highest": 180000 },
  "India": { "base": 600000, "average": 1200000, "highest": 3000000 },
  "Canada": { "base": 80000, "average": 110000, "highest": 150000 },
  "UK": { "base": 60000, "average": 85000, "highest": 130000 },
  "Germany": { "base": 60000, "average": 90000, "highest": 130000 },
  "China": { "base": 120000, "average": 200000, "highest": 350000 },
  "Japan": { "base": 6000000, "average": 8500000, "highest": 15000000 },
  "South Korea": { "base": 50000000, "average": 70000000, "highest": 100000000 },
  "Australia": { "base": 80000, "average": 110000, "highest": 150000 },
  "Singapore": { "base": 70000, "average": 100000, "highest": 150000 },
  "Sweden": { "base": 55000, "average": 80000, "highest": 120000 },
  "Netherlands": { "base": 60000, "average": 85000, "highest": 120000 },
  "Switzerland": { "base": 100000, "average": 130000, "highest": 180000 },
  "France": { "base": 55000, "average": 80000, "highest": 120000 },
  "Israel": { "base": 75000, "average": 100000, "highest": 150000 }
}

cybersecurity_engineer_salary_by_country = {
  "USA": { "base": 80000, "average": 110000, "highest": 150000 },
  "India": { "base": 600000, "average": 1200000, "highest": 3000000 },
  "Canada": { "base": 70000, "average": 95000, "highest": 130000 },
  "UK": { "base": 55000, "average": 80000, "highest": 120000 },
  "Germany": { "base": 60000, "average": 85000, "highest": 120000 },
  "China": { "base": 120000, "average": 200000, "highest": 350000 },
  "Japan": { "base": 5000000, "average": 7000000, "highest": 10000000 },
  "South Korea": { "base": 45000000, "average": 65000000, "highest": 90000000 },
  "Australia": { "base": 75000, "average": 105000, "highest": 140000 },
  "Singapore": { "base": 65000, "average": 95000, "highest": 130000 },
  "Sweden": { "base": 50000, "average": 75000, "highest": 110000 },
  "Netherlands": { "base": 55000, "average": 80000, "highest": 110000 },
  "Switzerland": { "base": 90000, "average": 120000, "highest": 170000 },
  "France": { "base": 50000, "average": 70000, "highest": 100000 },
  "Israel": { "base": 75000, "average": 100000, "highest": 150000 }
}

ethical_hacker_salary_by_country = {
  "USA": { "base": 70000, "average": 95000, "highest": 130000 },
  "India": { "base": 500000, "average": 1000000, "highest": 2500000 },
  "Canada": { "base": 60000, "average": 85000, "highest": 120000 },
  "UK": { "base": 50000, "average": 75000, "highest": 110000 },
  "Germany": { "base": 55000, "average": 80000, "highest": 110000 },
  "China": { "base": 100000, "average": 180000, "highest": 300000 },
  "Japan": { "base": 4500000, "average": 6000000, "highest": 9500000 },
  "South Korea": { "base": 40000000, "average": 60000000, "highest": 80000000 },
  "Australia": { "base": 65000, "average": 95000, "highest": 130000 },
  "Singapore": { "base": 60000, "average": 90000, "highest": 120000 },
  "Sweden": { "base": 45000, "average": 70000, "highest": 100000 },
  "Netherlands": { "base": 50000, "average": 75000, "highest": 110000 },
  "Switzerland": { "base": 85000, "average": 120000, "highest": 160000 },
  "France": { "base": 45000, "average": 70000, "highest": 100000 },
  "Israel": { "base": 65000, "average": 90000, "highest": 130000 }
}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict_salary")
async def predict_salary(data: SalaryPredictionRequest):
    if data.job_title.lower() == "software engineer":
        country = data.country
        if country in software_engineer_salary_by_country:
            salary_info = software_engineer_salary_by_country[country]

            if data.experience <= 2:
                salary = salary_info["base"]
            elif 3 <= data.experience <= 7:
                salary = salary_info["average"]
            elif 7 <= data.experience <= 10:
                salary = salary_info["highest"]
            return {"predicted_data": f"Based on your experince salary in {country} is ${salary:,}"}

        else:
            return {"predicted_data": "Country data not available for Software Engineer"}
    
    elif data.job_title.lower() == "full-stack developer":
        country = data.country
        if country in full_stack_developer_salary_by_country:
            salary_info = full_stack_developer_salary_by_country[country]

            if data.experience <= 2:
                salary = salary_info["base"]
            elif 3 <= data.experience <= 7:
                salary = salary_info["average"]
            elif 7 <= data.experience <= 10:
                salary = salary_info["highest"]
            return {"predicted_data": f"Based on your experince salary in {country} is ${salary:,}"}
        else:
            return {"predicted_data": "Country data not available for Full_stack developer"}
    
    elif data.job_title.lower() == "frontend developer":
        country = data.country
        if country in frontend_developer_salary_by_country:
            salary_info = frontend_developer_salary_by_country[country]

            if data.experience <= 2:
                salary = salary_info["base"]
            elif 3 <= data.experience <= 7:
                salary = salary_info["average"]
            elif 7 <= data.experience <= 10:
                salary = salary_info["highest"]
            return {"predicted_data": f"Based on your experince salary in {country} is ${salary:,}"}
        else:
            return {"predicted_data": "Country data not available for Frontend developer"}
        
    elif data.job_title.lower() == "backend developer":
        country = data.country
        if country in backend_developer_salary_by_country:
            salary_info = backend_developer_salary_by_country[country]

            if data.experience <= 2:
                salary = salary_info["base"]
            elif 3 <= data.experience <= 7:
                salary = salary_info["average"]
            elif 7 <= data.experience <= 10:
                salary = salary_info["highest"]
            return {"predicted_data": f"Based on your experince salary in {country} is ${salary:,}"}
        else:
            return {"predicted_data": "Country data not available for Backend developer"}
        
    elif data.job_title.lower() == "mobile app developer":
        country = data.country
        if country in mobile_app_developer_salary_by_country:
            salary_info = mobile_app_developer_salary_by_country[country]

            if data.experience <= 2:
                salary = salary_info["base"]
            elif 3 <= data.experience <= 7:
                salary = salary_info["average"]
            elif 7 <= data.experience <= 10:
                salary = salary_info["highest"]
            return {"predicted_data": f"Based on your experince salary in {country} is ${salary:,}"}
        else:
            return {"predicted_data": "Country data not available for Mobile App developer"}
        
    elif data.job_title.lower() == "game developer":
        country = data.country
        if country in game_developer_salary_by_country:
            salary_info = game_developer_salary_by_country[country]

            if data.experience <= 2:
                salary = salary_info["base"]
            elif 3 <= data.experience <= 7:
                salary = salary_info["average"]
            elif 7 <= data.experience <= 10:
                salary = salary_info["highest"]
            return {"predicted_data": f"Based on your experince salary in {country} is ${salary:,}"}
        else:
            return {"predicted_data": "Country data not available for Game developer"}
        
    elif data.job_title.lower() == "embedded systems developer":
        country = data.country
        if country in embedded_system_developer_salary_by_country:
            salary_info = embedded_system_developer_salary_by_country[country]

            if data.experience <= 2:
                salary = salary_info["base"]
            elif 3 <= data.experience <= 7:
                salary = salary_info["average"]
            elif 7 <= data.experience <= 10:
                salary = salary_info["highest"]
            return {"predicted_data": f"Based on your experince salary in {country} is ${salary:,}"}
        else:
            return {"predicted_data": "Country data not available for Embedded Systems developer"}
        
    elif data.job_title.lower() == "devops engineer":
        country = data.country
        if country in devops_engineer_salary_by_country:
            salary_info = devops_engineer_salary_by_country[country]

            if data.experience <= 2:
                salary = salary_info["base"]
            elif 3 <= data.experience <= 7:
                salary = salary_info["average"]
            elif 7 <= data.experience <= 10:
                salary = salary_info["highest"]
            return {"predicted_data": f"Based on your experince salary in {country} is ${salary:,}"}
        else:
            return {"predicted_data": "Country data not available for DevOps Engineer"}
        
    elif data.job_title.lower() == "ai engineer":
        country = data.country
        if country in ai_engineer_salary_by_country:
            salary_info = ai_engineer_salary_by_country[country]

            if data.experience <= 2:
                salary = salary_info["base"]
            elif 3 <= data.experience <= 7:
                salary = salary_info["average"]
            elif 7 <= data.experience <= 10:
                salary = salary_info["highest"]
            return {"predicted_data": f"Based on your experince salary in {country} is ${salary:,}"}
        else:
            return {"predicted_data": "Country data not available for AI Engineer"}
        
    elif data.job_title.lower() == "data scientist":
        country = data.country
        if country in data_scientist_salary_by_country:
            salary_info = data_scientist_salary_by_country[country]

            if data.experience <= 2:
                salary = salary_info["base"]
            elif 3 <= data.experience <= 7:
                salary = salary_info["average"]
            elif 7 <= data.experience <= 10:
                salary = salary_info["highest"]
            return {"predicted_data": f"Based on your experince salary in {country} is ${salary:,}"}
        else:
            return {"predicted_data": "Country data not available for Data Scientist"}
        
    elif data.job_title.lower() == "data analyst":
        country = data.country
        if country in data_analyst_salary_by_country:
            salary_info = data_analyst_salary_by_country[country]

            if data.experience <= 2:
                salary = salary_info["base"]
            elif 3 <= data.experience <= 7:
                salary = salary_info["average"]
            elif 7 <= data.experience <= 10:
                salary = salary_info["highest"]
            return {"predicted_data": f"Based on your experince salary in {country} is ${salary:,}"}
        else:
            return {"predicted_data": "Country data not available for Data Analyst"}
        
    elif data.job_title.lower() == "machine learning engineer":
        country = data.country
        if country in machine_learning_engineer_salary_by_country:
            salary_info = machine_learning_engineer_salary_by_country[country]

            if data.experience <= 2:
                salary = salary_info["base"]
            elif 3 <= data.experience <= 7:
                salary = salary_info["average"]
            elif 7 <= data.experience <= 10:
                salary = salary_info["highest"]
            return {"predicted_data": f"Based on your experince salary in {country} is ${salary:,}"}
        else:
            return {"predicted_data": "Country data not available for Machine Learning Engineer"}
        
    elif data.job_title.lower() == "cybersecurity engineer":
        country = data.country
        if country in cybersecurity_engineer_salary_by_country:
            salary_info = cybersecurity_engineer_salary_by_country[country]

            if data.experience <= 2:
                salary = salary_info["base"]
            elif 3 <= data.experience <= 7:
                salary = salary_info["average"]
            elif 7 <= data.experience <= 10:
                salary = salary_info["highest"]
            return {"predicted_data": f"Based on your experince salary in {country} is ${salary:,}"}
        else:
            return {"predicted_data": "Country data not available for Cybersecurity developer"}
        
    elif data.job_title.lower() == "ethical hacker":
        country = data.country
        if country in ethical_hacker_salary_by_country:
            salary_info = ethical_hacker_salary_by_country[country]

            if data.experience <= 2:
                salary = salary_info["base"]
            elif 3 <= data.experience <= 7:
                salary = salary_info["average"]
            elif 7 <= data.experience <= 10:
                salary = salary_info["highest"]
            return {"predicted_data": f"Based on your experince salary in {country} is ${salary:,}"}
        else:
            return {"predicted_data": "Country data not available for Ethical Hacker"}

    else:
        return{"predicted_data":"Please Select Job Role and Other Details !"}
