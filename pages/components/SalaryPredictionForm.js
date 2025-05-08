import { useState } from "react";
import { useForm } from "react-hook-form";
import axios from "axios";
import Select from "react-select";
import Image from "next/image"; 

const jobRoles = [
  { value: "Software Engineer", label: "Software Engineer" },
  { value: "Full-Stack Developer", label: "Full-Stack Developer" },
  { value: "Frontend Developer", label: "Frontend Developer" },
  { value: "Backend Developer", label: "Backend Developer" },
  { value: "Mobile App Developer", label: "Mobile App Developer" },
  { value: "Game Developer", label: "Game Developer" },
  { value: "Embedded Systems Developer", label: "Embedded Systems Developer" },
  { value: "DevOps Engineer", label: "DevOps Engineer" },
  { value: "AI Engineer", label: "AI Engineer" },
  { value: "Data Scientist", label: "Data Scientist" },
  { value: "Data Analyst", label: "Data Analyst" },
  { value: "Machine Learning Engineer", label: "Machine Learning Engineer" },
  { value: "Cybersecurity Engineer", label: "Cybersecurity Engineer" },
  { value: "Ethical Hacker", label: "Ethical Hacker" },
];


const industries = [
  { value: "Technology", label: "Technology" },
  { value: "Healthcare", label: "Healthcare" },
  { value: "Finance", label: "Finance" },
  { value: "Education", label: "Education" },
  { value: "Manufacturing", label: "Manufacturing" },
];

const experience = [
    { value: "0 year", label: "0 year" },
    { value: "1 year", label: "1 year" },
    { value: "2 year", label: "2 year" },
    { value: "3 year", label: "3 year" },
    { value: "4 year", label: "4 year" },
    { value: "5 year", label: "5 year" },
    { value: "6 year", label: "6 year" },
    { value: "7 year", label: "7 year" },
    { value: "8 year", label: "8 year" },
    { value: "9 year", label: "9 year" },
    { value: "10 year +", label: "10 year +" },
  ];

const educationLevels = [
  { value: "High School", label: "High School" },
  { value: "Bachelor's Degree", label: "Bachelor's Degree" },
  { value: "Master's Degree", label: "Master's Degree" },
  { value: "PhD", label: "PhD" },
];

const companyTypes = [
  { value: "Startup", label: "Startup" },
  { value: "Small Business", label: "Small Business" },
  { value: "MNC", label: "MNC" },
  { value: "Government", label: "Government" },
];

const skills = [
    { value: "A/B Testing", label: "A/B Testing" },
    { value: "AWS", label: "AWS" },
    { value: "Accessibility", label: "Accessibility" },
    { value: "Algorithms", label: "Algorithms" },
    { value: "Ansible", label: "Ansible" },
    { value: "Apache Spark", label: "Apache Spark" },
    { value: "App Deployment", label: "App Deployment" },
    { value: "Assembly Language", label: "Assembly Language" },
    { value: "Authentication", label: "Authentication" },
    { value: "Authorization", label: "Authorization" },
    { value: "Azure", label: "Azure" },
    { value: "Big Data", label: "Big Data" },
    { value: "Bloc", label: "Bloc" },
    { value: "Burp Suite", label: "Burp Suite" },
    { value: "C", label: "C" },
    { value: "C++", label: "C++" },
    { value: "CCNA", label: "CCNA" },
    { value: "CI/CD", label: "CI/CD" },
    { value: "CSS", label: "CSS" },
    { value: "Calculus", label: "Calculus" },
    { value: "Chakra UI", label: "Chakra UI" },
    { value: "Cisco", label: "Cisco" },
    { value: "Classification", label: "Classification" },
    { value: "Computer Vision", label: "Computer Vision" },
    { value: "Django", label: "Django" },
    { value: "DNS", label: "DNS" },
    { value: "Data Cleaning", label: "Data Cleaning" },
    { value: "Data Structures", label: "Data Structures" },
    { value: "Data Visualization", label: "Data Visualization" },
    { value: "Debugging", label: "Debugging" },
    { value: "Deep Learning", label: "Deep Learning" },
    { value: "Design Patterns", label: "Design Patterns" },
    { value: "Device Drivers", label: "Device Drivers" },
    { value: "Docker", label: "Docker" },
    { value: "ETL", label: "ETL" },
    { value: "Excel", label: "Excel" },
    { value: "Exploratory Data Analysis", label: "Exploratory Data Analysis" },
    { value: "FastAPI", label: "FastAPI" },
    { value: "Feature Engineering", label: "Feature Engineering" },
    { value: "Firebase", label: "Firebase" },
    { value: "Firewalls", label: "Firewalls" },
    { value: "Flask", label: "Flask" },
    { value: "Flutter", label: "Flutter" },
    { value: "GCP", label: "GCP" },
    { value: "Game Loops", label: "Game Loops" },
    { value: "Game Physics", label: "Game Physics" },
    { value: "Git", label: "Git" },
    { value: "GitHub", label: "GitHub" },
    { value: "Grafana", label: "Grafana" },
    { value: "GraphQL", label: "GraphQL" },
    { value: "Hadoop", label: "Hadoop" },
    { value: "HTML", label: "HTML" },
    { value: "Horovod", label: "Horovod" },
    { value: "IAM", label: "IAM" },
    { value: "Incident Response", label: "Incident Response" },
    { value: "I2C", label: "I2C" },
    { value: "Java", label: "Java" },
    { value: "JavaScript", label: "JavaScript" },
    { value: "Jenkins", label: "Jenkins" },
    { value: "Jupyter notebooks", label: "Jupyter notebooks" },
    { value: "Juniper", label: "Juniper" },
    { value: "Kafka", label: "Kafka" },
    { value: "Kali Linux", label: "Kali Linux" },
    { value: "Kubernetes", label: "Kubernetes" },
    { value: "Linux", label: "Linux" },
    { value: "Load balancing", label: "Load balancing" },
    { value: "Machine Learning", label: "Machine Learning" },
    { value: "Malware Analysis", label: "Malware Analysis" },
    { value: "Matplotlib", label: "Matplotlib" },
    { value: "Metasploit", label: "Metasploit" },
    { value: "Microcontrollers", label: "Microcontrollers" },
    { value: "Microservices", label: "Microservices" },
    { value: "MLOps", label: "MLOps" },
    { value: "Model Deployment", label: "Model Deployment" },
    { value: "Model optimization", label: "Model optimization" },
    { value: "MongoDB", label: "MongoDB" },
    { value: "Multiplayer Networking", label: "Multiplayer Networking" },
    { value: "NLP", label: "NLP" },
    { value: "Nmap", label: "Nmap" },
    { value: "Next.js", label: "Next.js" },
    { value: "Node.js", label: "Node.js" },
    { value: "NumPy", label: "NumPy" },
    { value: "OWASP", label: "OWASP" },
    { value: "Pandas", label: "Pandas" },
    { value: "Penetration Testing", label: "Penetration Testing" },
    { value: "Performance Optimization", label: "Performance Optimization" },
    { value: "PostgreSQL", label: "PostgreSQL" },
    { value: "Power BI", label: "Power BI" },
    { value: "Probability", label: "Probability" },
    { value: "Prometheus", label: "Prometheus" },
    { value: "Push Notifications", label: "Push Notifications" },
    { value: "PyTorch", label: "PyTorch" },
    { value: "Python", label: "Python" },
    { value: "R", label: "R" },
    { value: "RabbitMQ", label: "RabbitMQ" },
    { value: "React", label: "React" },
    { value: "React Native", label: "React Native" },
    { value: "Realtime Apps", label: "Realtime Apps" },
    { value: "Recommender Systems", label: "Recommender Systems" },
    { value: "Redis", label: "Redis" },
    { value: "Red Teaming", label: "Red Teaming" },
    { value: "Regression", label: "Regression" },
    { value: "Redux", label: "Redux" },
    { value: "REST APIs", label: "REST APIs" },
    { value: "RTOS", label: "RTOS" },
    { value: "Scripting", label: "Scripting" },
    { value: "Scikit-learn", label: "Scikit-learn" },
    { value: "Seaborn", label: "Seaborn" },
    { value: "Secure Coding", label: "Secure Coding" },
    { value: "Shader", label: "Shader" },
    { value: "Shell Scripting", label: "Shell Scripting" },
    { value: "SIEM", label: "SIEM" },
    { value: "SQL", label: "SQL" },
    { value: "SPI", label: "SPI" },
    { value: "Splunk", label: "Splunk" },
    { value: "Statistics", label: "Statistics" },
    { value: "Subnetting", label: "Subnetting" },
    { value: "Svelte", label: "Svelte" },
    { value: "Swift", label: "Swift" },
    { value: "System Design", label: "System Design" },
    { value: "Tableau", label: "Tableau" },
    { value: "Tailwind CSS", label: "Tailwind CSS" },
    { value: "TCP/IP", label: "TCP/IP" },
    { value: "Terraform", label: "Terraform" },
    { value: "TensorFlow", label: "TensorFlow" },
    { value: "Threat Hunting", label: "Threat Hunting" },
    { value: "Time Series", label: "Time Series" },
    { value: "TypeScript", label: "TypeScript" },
    { value: "UART", label: "UART" },
    { value: "UI/UX", label: "UI/UX" },
    { value: "Unity", label: "Unity" },
    { value: "Unreal Engine", label: "Unreal Engine" },
    { value: "Vercel", label: "Vercel" },
    { value: "VPNs", label: "VPNs" },
    { value: "Vue.js", label: "Vue.js" },
    { value: "Wireshark", label: "Wireshark" }
  ];
  
  const countries = [
    { value: "USA", label: "USA" },
    { value: "India", label: "India" },
    { value: "Canada", label: "Canada" },
    { value: "UK", label: "UK" },
    { value: "Germany", label: "Germany" },
    { value: "China", label: "China" },
    { value: "Japan", label: "Japan" },
    { value: "South Korea", label: "South Korea" },
    { value: "Australia", label: "Australia" },
    { value: "Singapore", label: "Singapore" },
    { value: "Sweden", label: "Sweden" },
    { value: "Netherlands", label: "Netherlands" },
    { value: "Switzerland", label: "Switzerland" },
    { value: "France", label: "France" },
    { value: "Israel", label: "Israel" }
  ];
  
  const salaryOptions = [
    { value: "0", label: "$0" },
    { value: "10000", label: "$10,000" },
    { value: "20000", label: "$20,000" },
    { value: "30000", label: "$30,000" },
    { value: "40000", label: "$40,000" },
    { value: "50000", label: "$50,000" },
    { value: "60000", label: "$60,000" },
    { value: "70000", label: "$70,000" },
    { value: "80000", label: "$80,000" },
    { value: "90000", label: "$90,000" },
    { value: "100000", label: "$100,000+" },
  ];
  
const SalaryPredictionForm = ({ onSubmit }) => {
    const [selectedJobRole, setSelectedJobRole] = useState("");
    const [selectedIndustry, setSelectedIndustry] = useState("");
    const [selectedExperience, setSelectedExperience] = useState("");
    const [selectedEducation, setSelectedEducation] = useState("");
    const [selectedCompanyType, setSelectedCompanyType] = useState("");
    const [selectedSkills, setSelectedSkills] = useState([]);
    const [selectedCountry, setSelectedCountry] = useState("");
    const [selectedCurrentSalary, setSelectedCurrentSalary] = useState(null);
    const { register, handleSubmit, control } = useForm();
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const onSubmitForm = async (event) => {
        if (event && event.preventDefault) event.preventDefault();
    
        const formData = {
            job_title: selectedJobRole?.value || "",
            industry: selectedIndustry?.value || "",
            experience: parseInt(selectedExperience?.value || "0"),

            country: selectedCountry?.value || "",
        };
    
        console.log("Sending data:", formData);  // Debugging step
    
        try {
            const response = await axios.post("http://127.0.0.1:8000/predict_salary", formData);
            alert(` ${response.data.predicted_data}`);
        } catch (error) {
            console.error("Error predicting salary:", error);
        }
    };
    
    
    

  return (
    <form className="text-white p-6 rounded-lg shadow-lg max-w-lg mx-auto items-center content-center" onSubmit={handleSubmit(onSubmitForm)}>
        {error && <p className="text-red-500">{error}</p>}
        {loading && <p className="text-blue-500">Loading...</p>}
        <div className="grid grid-cols-2 gap-4">
            
            <div>
                <label style={{fontSize:"20px"}} htmlFor="education" className="block mb-2 font-medium text-white">
                    Job Title
                </label>
                <select style={{ backgroundColor:"black", border: "2px solid", fontSize:"20px",}}
                value={selectedJobRole?.value || ""} 
                onChange={(e) => {
                    const selectedOption = jobRoles.find(option => option.value === e.target.value);
                    setSelectedJobRole(selectedOption);
                }}
                
                id="education"
                className="bg-gray-900 border border-gray-600 text-white text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                >
                    <option value="" disabled>Select</option>
                    {jobRoles.map(option => (
                    <option key={option.value} value={option.value}>
                    {option.label}
                    </option>
                    ))}
                </select>
            </div>
        
            <div>
                <label style={{fontSize:"20px"}} htmlFor="education" className="block mb-2 font-medium text-white">
                    Industries
                </label>
                <select style={{backgroundColor:"black", border: "2px solid", fontSize:"20px",}}
                value={selectedIndustry?.value || ""}
                onChange={(e) => {
                    const selectedOption = industries.find(option => option.value === e.target.value);
                    setSelectedIndustry(selectedOption);
                  }}
                
                id="education"
                className="bg-gray-900 border border-gray-600 text-white text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                >
                    <option value="" disabled>Select</option>
                    {industries.map(option => (
                    <option key={option.value} value={option.value}>
                    {option.label}
                    </option>
                    ))}
                </select>
            </div>

            <div>
                <label style={{fontSize:"20px"}} htmlFor="education" className="block mb-2 font-medium text-white">
                    Experience
                </label>
                <select style={{backgroundColor:"black", border: "2px solid", fontSize:"20px",}}
                value={selectedExperience?.value || ""}
                onChange={(e) => {
                    const selectedOption = experience.find(option => option.value === e.target.value);
                    setSelectedExperience(selectedOption);
                  }}
                  
                id="education"
                className="bg-gray-900 border border-gray-600 text-white text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                >
                    <option value="" disabled>Select</option>
                    {experience.map(option => (
                    <option key={option.value} value={option.value}>
                    {option.label}
                    </option>
                    ))}
                </select>
            </div>

            <div>
                <label style={{fontSize:"20px"}} htmlFor="education" className="block mb-2 font-medium text-white">
                    Country
                </label>
                <select style={{backgroundColor:"black", border: "2px solid", fontSize:"20px",}}
                value={selectedCountry?.value || ""}
                onChange={(e) => {
                    const selectedOption = countries.find(option => option.value === e.target.value);
                    setSelectedCountry(selectedOption);
                  }}
                  
                id="education"
                className="bg-gray-900 border border-gray-600 text-white text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
                >
                    <option value="" disabled>Select</option>
                    {countries.map(option => (
                    <option key={option.value} value={option.value}>
                    {option.label}
                    </option>
                    ))}
                </select>
            </div>

        </div>
        <div style={{paddingTop:"25px",justifyContent:"center", alignItems:"center",display:"flex"}}>
        <button type="submit" style={{border:"3px solid #1E90FF",backgroundColor:"black",paddingLeft:"10px", paddingRight:"10px", borderRadius:"50px"}} className="flex text-white cursor-pointer rounded-full hover:scale-110 transition-transform duration-300 ease-in-out" disabled={loading}>
        {loading ? "Submitting..." : "Submit"}
        </button>
        </div>
</form>

  );
};

export default SalaryPredictionForm;
