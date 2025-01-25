// lib/api.ts
const API_BASE_URL = 'http://localhost:3000'; // Replace with your backend URL

export const predictStockMovement = async (data: any) => {
    const response = await fetch(`${API_BASE_URL}/predict`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });
    if (!response.ok) {
        throw new Error('Failed to fetch prediction');
    }
    return response.json();
};

export const fetchSentiment = async () => {
    const response = await fetch(`${API_BASE_URL}/sentiment`);
    if (!response.ok) {
        throw new Error('Failed to fetch sentiment data');
    }
    return response.json();
};

export const recommendStrategy = async (data: any) => {
    const response = await fetch(`${API_BASE_URL}/recommend`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });
    if (!response.ok) {
        throw new Error('Failed to fetch recommendation');
    }
    return response.json();
};