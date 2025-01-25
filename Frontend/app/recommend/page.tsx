import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

export default function RecommendPage() {
  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold mb-8 text-center">AI Portfolio Insights</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8">
        <Card>
          <CardHeader>
            <CardTitle>Sentiment Analysis</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-lg mb-4">
              Current market sentiment: <span className="font-bold text-green-500">Positive</span>
            </p>
            <p>
              Based on recent news and social media trends, the overall market sentiment appears to be optimistic. This
              could indicate potential growth opportunities in certain sectors.
            </p>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Portfolio Recommendation</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-lg mb-4">
              Suggested action: <span className="font-bold text-blue-500">Diversify</span>
            </p>
            <p>
              Our AI analysis suggests that diversifying your portfolio across different sectors could help mitigate
              risks and potentially increase returns in the current market conditions.
            </p>
          </CardContent>
        </Card>
      </div>

      {/* You can add more cards or components here for additional insights */}
    </div>
  )
}

