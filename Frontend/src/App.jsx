import React from "react";
import { Route, BrowserRouter as Router } from "react-router-dom";
import Navbar from "./components/Navbar";
import HeroSection from "./components/HeroSection";
import AiFeatureSection from "./components/AiFeatureSection";
import MarketInsight from "./components/MarketInsight";
import LearningHub from "./components/LearningHub";
import Footer from "./components/Footer";
function App() {
  return (
    <Router>
      <Navbar />
      <HeroSection />
      <AiFeatureSection />
      <MarketInsight />
      <LearningHub />
      <Footer />
    </Router>
  );
}

export default App;
