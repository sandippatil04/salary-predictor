import Link from "next/link";
import Image from "next/image";

export default function Footer() {
    return (
        <footer className="bg-gray-900 text-white w-full py-6 flex justify-center">
            <div className="container mx-auto flex flex-col items-center space-y-6">
                {/* Footer Title */}
                <h2 style={{fontSize: "25px", paddingTop:"20px",paddingBottom:"20px"}} className="text-2xl md:text-3xl font-bold text-center mb-6">
                    SkillSight AI by <span className="text-blue-400">Sandip Patil</span>
                </h2>

                {/* Social Media Icons */}
                <div className="flex flex-wrap justify-center gap-8 mt-6">
                    <Link href="https://www.linkedin.com/in/sandippatil04/" target="_blank" rel="noopener noreferrer">
                        <Image
                            width={30} height={30}
                            src="/images/linkedin.png"
                            alt="LinkedIn"
                            className="hover:scale-110 transition-transform duration-300 hover:shadow-[0_0_20px_#0A66C2]"
                        />
                    </Link>
                    <Link href="https://x.com/sandippatil_04" target="_blank" rel="noopener noreferrer">
                        <Image
                            width={30} height={30}
                            src="/images/twitter.png"
                            alt="Twitter"
                            className="hover:scale-110 transition-transform duration-300 hover:shadow-[0_0_20px_#1DA1F2]"
                        />
                    </Link>
                    <Link href="https://www.instagram.com/its_sandippatil/#" target="_blank" rel="noopener noreferrer">
                        <Image
                            width={30} height={30}
                            src="/images/instagram.png"
                            alt="Instagram"
                            className="hover:scale-110 transition-transform duration-300 hover:shadow-[0_0_20px_#E1306C]"
                        />
                    </Link>
                    <Link href="https://www.facebook.com/itssandippatil" target="_blank" rel="noopener noreferrer">
                        <Image
                            width={30} height={30}
                            src="/images/facebook.png"
                            alt="Facebook"
                            className="hover:scale-110 transition-transform duration-300 hover:shadow-[0_0_20px_#1877F2]"
                        />
                    </Link>
                </div>

                {/* Copyright */}
                <p style={{paddingTop:"10px"}} className="text-sm text-gray-400 mt-6">&copy; {new Date().getFullYear()} SkillSight AI. All rights reserved.</p>
            </div>
        </footer>
    );
}
