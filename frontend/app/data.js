export async function test() {
    try {
        const response = await fetch("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=VTI&apikey=2GS25PVYA0IK4RH2");
        const data = await response.json();
        
        // Safely access the data and extract the last 5 closing prices
        const dailyData = data['Time Series (Daily)'];
        if (!dailyData) {
            throw new Error("Missing 'Time Series (Daily)' in response");
        }

        // Use Object.values to simplify extraction and slice to get the first 5 entries
        const closingPrices = Object.values(dailyData)
            .slice(0, 5)
            .map(entry => entry['4. close']);
        console.log(closingPrices)
        return closingPrices;
    } catch (error) {
        console.error("Error in test function:", error);
        throw error; // Re-throw error to handle it in fetchData
    }
}




