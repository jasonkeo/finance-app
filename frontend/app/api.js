import dotenv from 'dotenv';

dotenv.config();
export default async function get() {
    const today = new Date();
    const formattedToday = today.toISOString().split('T')[0];
    const url = 'https://ilovepickles.cc/api/news/';
    
    try {
        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });

       
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        
        for (let i = data.length - 1; i > 0; i--) {
            if (data[i]['date'] == formattedToday) {
                console.log(data[i])
                return data[i];
            
            }
        }
        console.log(data[data.length - 1])
        return data[data.length - 1];
        
        
    } catch (error) {
        console.error('Error fetching data:', error);
        return(['Error']);
    }
}