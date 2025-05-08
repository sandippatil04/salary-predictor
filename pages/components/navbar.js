"use client";
import Link from "next/link";
import { useState } from "react";

export default function Navbar() {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const toggleMobileMenu = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen);
  };

  const scrollToSection = (id) => {
    setTimeout(() => {
      const section = document.getElementById(id);
      if (section) {
        section.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    }, 200); // Adjust delay if needed
  };

  // Navigation items
  const navItems = [
    { name: "Home", href: "#home" },
    { name: "Service", href: "#service" },
    { name: "About", href: "#about" },
    { name: "Contact", href: "#contact" },
  ];

  return (
    <div>
      <nav style={{height:"50px",paddingTop:"10px", paddingLeft: "30px", paddingRight: "100px" }} className=" block w-full max-w-screen px-6 py-6 mx-auto bg-white bg-opacity-90 fixed shadow-2xl lg:px-12 xl:px-20 backdrop-blur-lg backdrop-saturate-150 z-[9999]">
        <div className="container flex flex-wrap items-center justify-between mx-auto text-slate-800">
          <Link href="/" className="mr-12 block cursor-pointer py-3 text-red-600 font-bold text-3xl">
            SkillSight AI
          </Link>

          <div className="lg:hidden">
            <button onClick={toggleMobileMenu} className="relative ml-auto h-10 w-10 select-none rounded-lg text-center text-xs font-medium text-inherit transition-all hover:bg-transparent">
              <span className="absolute transform -translate-x-1/2 -translate-y-1/2 top-1/2 left-1/2">
                <svg xmlns="http://www.w3.org/2000/svg" className="w-12 h-12" fill="none" stroke="currentColor" strokeWidth="2">
                  <path strokeLinecap="round" strokeLinejoin="round" d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
              </span>
            </button>
          </div>

          {/* Mobile Menu */}
          <div className={`fixed top-0 left-0 min-h-screen w-80 bg-slate-100 shadow-2xl transform transition-transform duration-300 ease-in-out ${isMobileMenuOpen ? "translate-x-0" : "-translate-x-full"} lg:hidden z-50`}>
            <div className="flex flex-row items-center border-b pb-6 px-6">
              <Link href="/" className="cursor-pointer text-red-600 font-bold text-2xl pt-6">
                SkillSight AI
              </Link>
              <button onClick={toggleMobileMenu} className="absolute top-6 right-6 text-slate-600 hover:text-red-500">
                <svg xmlns="http://www.w3.org/2000/svg" className="w-10 h-10" fill="none" stroke="currentColor" strokeWidth="2">
                  <path strokeLinecap="round" strokeLinejoin="round" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
            <ul className="flex flex-col h-full space-y-8 p-8">
              {navItems.map((item, index) => (
                <li key={index} className="flex items-center px-8 py-4 text-xl gap-x-6 text-slate-600 hover:text-red-500">
                  <button onClick={() => scrollToSection(item.href.replace("#", ""))} className="flex items-center">
                    {item.name}
                  </button>
                </li>
              ))}
            </ul>
          </div>

          {/* Desktop Menu */}
          <div className="hidden lg:block">
            <ul className="flex flex-col gap-6 mt-4 mb-6 lg:mb-0 lg:mt-0 lg:flex-row lg:items-center lg:gap-16">
              {navItems.map((item, index) => (
                <li key={index} className="flex items-center px-10 py-4 text-xl gap-x-8 text-slate-600 hover:text-red-500">
                  <button onClick={() => scrollToSection(item.href.replace("#", ""))} className="cursor-pointer flex items-center">
                    {item.name}
                  </button>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </nav>
    </div>
  );
}
