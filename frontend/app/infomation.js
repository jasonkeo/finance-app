import dotenv from 'dotenv';

dotenv.config();
export default async function get() {
    const today = new Date();
    const formattedToday = today.toISOString().split('T')[0];
    const backend = process.env.BACKEND? process.env.BACKEND : '209.38.80.23';
    const url = `http://localhost:8000/api/news/`;
    try {
        const response = await fetch(url); // Replace with your API URL
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        for (let i = data.length - 1; i > 0; i--) {
            if (data[i]['date'] == formattedToday) {
                return data[i]['news'];
            }
        }
        return data[data.length - 1]['news'];
        
    } catch (error) {
        console.error('Error fetching data:', error);
        return(['Error']);
    }
}
