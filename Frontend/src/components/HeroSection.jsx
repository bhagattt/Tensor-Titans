import React from "react";
import heroImage from "../assets/hero_message.png"; // Replace with your image path
import Dashboard from "../pages/Dashboard";
import { Link } from "react-router-dom";
function HeroSection() {
  return (
    <div className="relative bg-gray-900">
      {" "}
      {/* Add padding-top to avoid overlap with navbar */}
      <img
        src={heroImage}
        alt=""
        className="w-full h-auto rounded-lg object-cover"
      />
      <div className="absolute inset-0 flex flex-col items-center justify-center px-4 sm:px-6 lg:px-12">
        <div
          className="text-center bg-black bg-opacity-30 p-4 sm:p-6 rounded-lg text-white animate-fade-in-right"
          style={{ animation: "fadeInRight 1s ease-in-out" }}
        >
          <h2 className="text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-extrabold mb-4">
            AI-Powered Wealth Management Made Simple
          </h2>
          <p className="text-sm sm:text-base md:text-lg lg:text-xl mb-6">
            Harness artificial intelligence to optimize your investments,
            predict market trends, and grow your wealth intelligently.
          </p>

          <Link
            to={Dashboard} // Dashboard would be the path like "/dashboard"
            className="inline-block bg-blue-600 text-white py-3 px-6 rounded-lg text-lg font-medium shadow-lg hover:bg-blue-700 transition duration-300"
          >
            Start Free Trial
          </Link>
        </div>
      </div>
      {/* Tailwind CSS animation */}
      <style>{`
        @keyframes fadeInRight {
          from {
            opacity: 0;
            transform: translateX(50px);
          }
          to {
            opacity: 1;
            transform: translateX(0);
          }
        }
        .animate-fade-in-right {
          animation: fadeInRight 1s ease-in-out;
        }
      `}</style>
    </div>
  );
}

export default HeroSection;
