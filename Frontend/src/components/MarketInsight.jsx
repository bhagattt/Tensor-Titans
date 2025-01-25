import React, { useEffect } from "react";
import {
  Chart as ChartJS,
  LineController,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend,
} from "chart.js";

// Register required components for a line chart
ChartJS.register(
  LineController,
  LineElement,
  PointElement,
  CategoryScale,
  LinearScale,
  Tooltip,
  Legend
);

const MarketInsight = () => {
  useEffect(() => {
    const ctx = document.getElementById("marketChart").getContext("2d");

    new ChartJS(ctx, {
      type: "line", // Ensure "line" is registered with LineController
      data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        datasets: [
          {
            label: "AI Market Index",
            data: [65, 59, 80, 81, 56, 55],
            borderColor: "#2dd4bf",
            tension: 0.4,
          },
        ],
      },
      options: {
        responsive: true,
        plugins: {
          legend: { position: "top" },
        },
      },
    });
  }, []);

  return (
    <section id="insights" className="py-20 bg-gray-50">
      <div className="container mx-auto px-6">
        <h2 className="text-4xl font-bold text-center mb-12">
          Live Market Intelligence
        </h2>
        <div className="grid md:grid-cols-2 gap-8">
          <div className="bg-white p-6 rounded-2xl shadow-sm">
            <canvas id="marketChart"></canvas>
          </div>
          <div className="space-y-6">
            <div className="ai-card p-6 rounded-xl">
              <h3 className="text-xl font-semibold mb-4">📈 Trending Assets</h3>
              <div className="space-y-4"></div>
            </div>
            <div className="ai-card p-6 rounded-xl">
              <h3 className="text-xl font-semibold mb-4">
                🔍 AI Recommendations
              </h3>
              <div className="space-y-4"></div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default MarketInsight;
