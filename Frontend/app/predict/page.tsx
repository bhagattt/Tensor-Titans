'use client'; // Mark this as a Client Component

import { useState } from 'react';
import { Input } from '@/components/ui/input';
import { Card, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button'; // Assuming you have a Button component
import { predictStockMovement } from '@/lib/api'; // Import the API utility

export default function PredictPage() {
  const [open, setOpen] = useState<number | string>('');
  const [high, setHigh] = useState<number | string>('');
  const [low, setLow] = useState<number | string>('');
  const [close, setClose] = useState<number | string>('');
  const [volume, setVolume] = useState<number | string>('');
  const [prediction, setPrediction] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setPrediction(null);

    try {
      // Prepare the input data
      const inputData = {
        Open: parseFloat(open as string),
        High: parseFloat(high as string),
        Low: parseFloat(low as string),
        Close: parseFloat(close as string),
        Volume: parseFloat(volume as string),
      };

      // Call the API
      const result = await predictStockMovement(inputData);
      setPrediction(result.prediction);
    } catch (err) {
      // Handle the error safely
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError('An unknown error occurred');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-4xl font-bold mb-8 text-center">Predict Market Movements</h1>

      <Card className="max-w-2xl mx-auto mb-8">
        <CardContent className="p-6">
          <blockquote className="text-xl italic text-center">
            "The stock market is filled with individuals who know the price of everything, but the value of nothing."
            <footer className="text-right mt-2">— Philip Fisher</footer>
          </blockquote>
        </CardContent>
      </Card>

      <form onSubmit={handleSubmit} className="max-w-xl mx-auto">
        <div className="space-y-4">
          {/* Open Price Input */}
          <Input
            type="number"
            placeholder="Open Price"
            value={open}
            onChange={(e) => setOpen(e.target.value)}
            className="w-full text-lg py-3"
            required
          />

          {/* High Price Input */}
          <Input
            type="number"
            placeholder="High Price"
            value={high}
            onChange={(e) => setHigh(e.target.value)}
            className="w-full text-lg py-3"
            required
          />

          {/* Low Price Input */}
          <Input
            type="number"
            placeholder="Low Price"
            value={low}
            onChange={(e) => setLow(e.target.value)}
            className="w-full text-lg py-3"
            required
          />

          {/* Close Price Input */}
          <Input
            type="number"
            placeholder="Close Price"
            value={close}
            onChange={(e) => setClose(e.target.value)}
            className="w-full text-lg py-3"
            required
          />

          {/* Volume Input */}
          <Input
            type="number"
            placeholder="Volume"
            value={volume}
            onChange={(e) => setVolume(e.target.value)}
            className="w-full text-lg py-3"
            required
          />

          {/* Submit Button */}
          <Button type="submit" disabled={loading} className="w-full text-lg py-3">
            {loading ? 'Predicting...' : 'Predict'}
          </Button>
        </div>
      </form>

      {/* Display Prediction Results */}
      {prediction && (
        <Card className="max-w-xl mx-auto mt-8">
          <CardContent className="p-6">
            <h2 className="text-2xl font-bold mb-4">Prediction Result</h2>
            <p className="text-lg">{prediction}</p>
          </CardContent>
        </Card>
      )}

      {/* Display Error Message */}
      {error && (
        <Card className="max-w-xl mx-auto mt-8 bg-red-100 border-red-400">
          <CardContent className="p-6">
            <h2 className="text-2xl font-bold mb-4 text-red-700">Error</h2>
            <p className="text-lg text-red-700">{error}</p>
          </CardContent>
        </Card>
      )}
    </div>
  );
}