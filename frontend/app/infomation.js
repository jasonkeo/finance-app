
export default async function get() {
    const today = new Date();
    const formattedToday = today.toISOString().split('T')[0];
    try {
        const response = await fetch('http://127.0.0.1:8000/api/news/'); // Replace with your API URL
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
        throw error;
    }
}