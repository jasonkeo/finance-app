
export default async function get() {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/news/'); // Replace with your API URL
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
}