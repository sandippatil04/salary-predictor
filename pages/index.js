import Navbar from "./components/navbar";
import Contact from "./components/contact";
import SalaryPredictionForm from "./components/SalaryPredictionForm";
import Image from "next/image"; 

export default function Home() {
    return (
        <div>
        <Navbar/>
        <div>
            <section id="home" className="h-screen flex items-center justify-center text-white text-3xl">
                    {/* Centered flex container */}
                    <div className="flex flex-col md:flex-row items-center justify-between w-full max-w-5xl px-6">
                        {/* Left Content */}
                        <div className="text-center md:text-left">
                            <h1 className="text-4xl font-bold mb-6">
                                Unlock Your Earning Potential: <br />
                                Discover Your Ideal Salary Today! <br />
                                <span className="text-red-500">SkillSight AI</span>
                            </h1>
                        </div>

                        {/* Right Image */}
                        <div className="flex justify-center">
                            <Image
                                src="/images/airobot.jpg"
                                alt="AI Robot"
                                width={400} // Adjust width as needed
                                height={400} // Adjust height as needed
                                className="rounded-full shadow-lg hover:scale-110 transition-transform duration-300 ease-in-out animate-pulse "

                            />
                        </div>
                    </div>
            </section>
            <section style={{
                backgroundImage: "url('/images/grid.png')",
                backgroundSize: "cover",
                backgroundPosition: "center",
                height: "100vh",
                }} id="service" className="h-screen flex items-center justify-center   text-white text-3xl">
                <h1></h1>
                <SalaryPredictionForm/>
            </section>
            <section id="about" className="h-screen flex items-center justify-center  text-white px-6 lg:px-20">
                <div className="container mx-auto flex flex-col lg:flex-row items-center gap-12">

                    {/* Left Side - Image */}
                    <div className="lg:w-1/2 flex justify-center">
                        <div className="relative">
                            <Image
                                src="/images/aipc.jpg"
                                alt="AI pc"
                                width={450}
                                height={450}
                                className="rounded-lg shadow-lg transition-transform transform hover:scale-110 duration-300"
                            />
                            <div className="absolute inset-0 w-full h-full bg-blue-500 opacity-20 rounded-lg blur-2xl"></div>
                        </div>
                    </div>

                    {/* Right Side - Text Content */}
                    <div style={{paddingRight:"20px"}} className="lg:w-1/2 space-y-6 text-center lg:text-left animate-fadeIn">
                        <h1 style={{fontSize:40, paddingBottom:"10px"}} className="">
                            About Us
                        </h1>
                        <p className="text-xl text-gray-300 leading-relaxed">
                            At <span className="text-blue-500 font-semibold">SkillSight AI</span>, we help you make informed career decisions with our AI-powered Salary Prediction tool.
                            Simply enter your details, and our model will estimate your expected salary based on industry trends and real-time market data.
                        </p>
                    </div>

                </div>
            </section>

            <section id="contact" className=" flex items-center justify-center text-white text-3xl">
                <Contact/>
            </section>
        </div>
        </div>
    );
}
