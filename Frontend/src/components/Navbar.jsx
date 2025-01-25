import React, { useState } from "react";
import logo from "../assets/logo.png";
import AuthForm from "../pages/AuthForm";

function Navbar() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [showAuthForm, setShowAuthForm] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const toggleAuthForm = () => {
    setShowAuthForm(!showAuthForm);
  };

  return (
    <div>
      <nav className="w-full top-0 z-50 bg-blue-800">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            {/* Logo */}
            <div className="flex-shrink-0 flex items-center space-x-2">
              <img src={logo} alt="Logo" className="h-20 w-20 mt-2" />
              <span className="text-lg font-bold text-white">
                FinanceFlex AI
              </span>
            </div>

            {/* Desktop Navigation */}
            <div className="hidden md:flex items-center space-x-8">
              <a
                href="#features"
                className="text-white hover:text-blue-200 transition-colors duration-200 font-medium"
              >
                Features
              </a>
              <a
                href="#insights"
                className="text-white hover:text-blue-200 transition-colors duration-200 font-medium"
              >
                Insights
              </a>
              <a
                href="#predict"
                className="text-white hover:text-blue-200 transition-colors duration-200 font-medium"
              >
                Predict
              </a>
            </div>

            {/* Right side buttons */}
            <div className="flex items-center space-x-4">
              <button
                onClick={toggleAuthForm}
                className="hidden md:block px-4 py-2 rounded-lg bg-white text-blue-800 hover:bg-blue-50 transition-colors duration-200 font-medium shadow-sm"
              >
                {showAuthForm ? "Close" : "Login"}
              </button>
              <button
                onClick={toggleMenu}
                className="md:hidden p-2 rounded-lg hover:bg-blue-700 transition-colors duration-200"
                aria-label="Toggle menu"
              >
                {isMenuOpen ? (
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    className="h-6 w-6 text-white"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M6 18L18 6M6 6l12 12"
                    />
                  </svg>
                ) : (
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    className="h-6 w-6 text-white"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth="2"
                      d="M4 6h16M4 12h16M4 18h16"
                    />
                  </svg>
                )}
              </button>
            </div>
          </div>
        </div>
      </nav>

      {/* Render AuthForm when Login button is clicked */}
      {showAuthForm && (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
          <div className="bg-white p-8 rounded-lg shadow-lg max-w-md w-full">
            <AuthForm isLogin={true} />
            <button
              onClick={toggleAuthForm}
              className="mt-4 w-full px-4 py-2 rounded-lg bg-blue-800 text-white hover:bg-blue-700 transition-colors duration-200 font-medium"
            >
              Close
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Navbar;
