"use client";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import MarketMoodIndex from "@/components/MarketMoodIndex";

export default function RecommendPage() {
  return (
    <div className="bg-gradient-to-r from-green-200 via-blue-200 to-green-100 min-h-screen p-8">
      {/* Header */}
      <header className="text-center mb-12">
        <h1 className="text-5xl font-bold text-gray-800 tracking-wide">AI Portfolio Insights</h1>
        <p className="text-xl text-gray-700 mt-4 max-w-3xl mx-auto">
          Empowering your investment decisions with real-time market sentiment and AI-driven recommendations.
        </p>
      </header>

      {/* Market Mood Index */}
      <section className="mb-12">
        <MarketMoodIndex />
      </section>

      {/* Cards Section */}
      <section className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        {/* Sentiment Analysis Card */}
        <Card className="shadow-lg hover:shadow-xl transition duration-300 ease-in-out bg-white rounded-lg border-t-4 border-green-500">
          <CardHeader>
            <CardTitle className="flex items-center">
              <span role="img" aria-label="Sentiment" className="text-3xl mr-2">😊</span>
              Sentiment Analysis
            </CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-gray-600">
              Current market sentiment: <span className="font-semibold text-green-500">Positive</span>
            </p>
            <p className="mt-4 text-gray-500">
              Based on recent news and social media trends, the overall market sentiment appears to be optimistic.
              This could indicate potential growth opportunities in certain sectors.
            </p>
          </CardContent>
        </Card>

        {/* Portfolio Recommendation Card */}
        <Card className="shadow-lg hover:shadow-xl transition duration-300 ease-in-out bg-white rounded-lg border-t-4 border-blue-500">
          <CardHeader>
            <CardTitle className="flex items-center">
              <span role="img" aria-label="Lightbulb" className="text-3xl mr-2">💡</span>
              Portfolio Recommendation
            </CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-gray-600">
              Suggested action: <span className="font-semibold text-blue-500">Diversify</span>
            </p>
            <p className="mt-4 text-gray-500">
              Our AI analysis suggests that diversifying your portfolio across different sectors could help mitigate risks
              and potentially increase returns in the current market conditions.
            </p>
          </CardContent>
        </Card>

        {/* Market Trends Card */}
        <Card className="shadow-lg hover:shadow-xl transition duration-300 ease-in-out bg-white rounded-lg border-t-4 border-orange-500">
          <CardHeader>
            <CardTitle className="flex items-center">
              <span role="img" aria-label="Chart" className="text-3xl mr-2">📈</span>
              Market Trends
            </CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-gray-600">
              Trending sectors: <span className="font-semibold text-orange-500">Tech, Green Energy</span>
            </p>
            <p className="mt-4 text-gray-500">
              The tech and green energy sectors are showing strong growth potential, driven by innovation and increasing
              demand for sustainable solutions.
            </p>
          </CardContent>
        </Card>

        {/* Risk Analysis Card */}
        <Card className="shadow-lg hover:shadow-xl transition duration-300 ease-in-out bg-white rounded-lg border-t-4 border-yellow-500">
          <CardHeader>
            <CardTitle className="flex items-center">
              <span role="img" aria-label="Money" className="text-3xl mr-2">💰</span>
              Risk Analysis
            </CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-gray-600">
              Risk level: <span className="font-semibold text-yellow-500">Moderate</span>
            </p>
            <p className="mt-4 text-gray-500">
              While the market shows potential, it's important to remain cautious and diversify your investments to manage risks effectively.
            </p>
          </CardContent>
        </Card>
      </section>

      {/* Footer */}
      <footer className="mt-16 text-center text-gray-500">
        <p>© 2023 AI Portfolio Insights. All rights reserved.</p>
      </footer>
    </div>
  );
}
