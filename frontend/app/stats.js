'use client'
import { LineChart } from '@mui/x-charts/LineChart';
import { useEffect, useState } from 'react';

export default function Stats({stats}) {
    const [dat, setDat] = useState([0,0,0,0,0]);
    const [time, setTime] = useState([0,0,0,0,0]);
    const [selectedOption, setSelectedOption] = useState("VOO");

    async function fetchData() {
        try {
            
            setDat(stats[selectedOption][0] || [0, 0, 0, 0, 0]);
            const dateObjects = stats[selectedOption][1].map(date => new Date(date));
            setTime(dateObjects|| [0, 0, 0, 0, 0]);
            
        } catch (error) {
            console.error("Error in fetchData function:", error);
        }
    }

    useEffect(() => {
        fetchData();
    }, [selectedOption, stats]);

    const handleSelectChange = (e) => {
        setSelectedOption(e.target.value);
    };

    return (
        <div className="p-5 bg-white lg:min-w-[500px] rounded-lg shadow-md transition-transform transition-shadow hover:shadow-custom hover:translate-y-[-4.30px]">
            <div className='flex justify-between'>
                <strong>Financial Indicator</strong>
                <select 
                    className="ml-2 p-1 border rounded" 
                    value={selectedOption} 
                    onChange={handleSelectChange}
                >
                    <option value="VOO">VOO</option>
                    <option value="VTI">VTI</option>
                    <option value="gdp">GDP</option>
                    <option value="unemployment">Unemployment</option>
                    <option value="cpi">CPI</option>
                    <option value="interest_rate">Interest rate</option>
                </select>
            </div>
            <LineChart
                xAxis={[
                    {
                        data: 
                            time
                        ,
                        scaleType: 'time', // Use a time scale for proper date handling
                    },
                ]}
                series={[
                    {
                        data: dat,
                    },
                ]}
                height={300}
                
            />
        </div>
    );
}
