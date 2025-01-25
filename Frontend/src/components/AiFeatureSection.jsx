import React from "react";

const AiFeatureSection = () => {
  const features = [
    {
      icon: "bx bx-brain",
      title: "Predictive Analytics",
      description:
        "Machine learning models analyze historical data to forecast market trends.",
      bgColor: "bg-teal-100",
      textColor: "text-teal-600",
    },
    {
      icon: "bx bx-line-chart",
      title: "Portfolio Optimization",
      description:
        "AI-driven asset allocation based on your risk profile and goals.",
      bgColor: "bg-purple-100",
      textColor: "text-purple-600",
    },
    {
      icon: "bx bx-bot",
      title: "24/7 Monitoring",
      description: "Real-time market tracking and instant anomaly detection.",
      bgColor: "bg-blue-100",
      textColor: "text-blue-600",
    },
  ];

  return (
    <section id="features" className="py-20 bg-white">
      <div className="container mx-auto px-6">
        <h2 className="text-4xl font-bold text-center mb-16">
          Smart Investment Features
        </h2>
        <div className="grid md:grid-cols-3 gap-12">
          {features.map((feature, index) => (
            <div key={index} className="ai-card p-8 rounded-2xl">
              <div
                className={`w-16 h-16 ${feature.bgColor} rounded-xl mb-6 flex items-center justify-center`}
              >
                <i
                  className={`${feature.icon} text-3xl ${feature.textColor}`}
                ></i>
              </div>
              <h3 className="text-2xl font-semibold mb-4">{feature.title}</h3>
              <p className="text-gray-600">{feature.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default AiFeatureSection;
