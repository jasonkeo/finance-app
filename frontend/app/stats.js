'use client'
import { LineChart } from '@mui/x-charts/LineChart';
import data from './data';
import { useEffect, useState } from 'react';

export default function Stats() {
    const [dat, setDat] = useState([1, 0, 0, 0, 0]);
    const [selectedOption, setSelectedOption] = useState("VOO");

    async function fetchData() {
        try {
            const fetchedData = await data();
            setDat(fetchedData[selectedOption].reverse() || [0, 0, 0, 0, 0]);
        } catch (error) {
            console.error("Error in fetchData function:", error);
        }
    }

    useEffect(() => {
        fetchData();
    }, [selectedOption]);

    const handleSelectChange = (e) => {
        setSelectedOption(e.target.value);
    };

    return (
        <div className="p-5 bg-white min-w-[500px] rounded-lg shadow-md transition-transform transition-shadow hover:shadow-custom hover:translate-y-[-4.30px]">
            <div className='flex justify-between'>
                Stats
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
                xAxis={[{ data: [1, 2, 3, 4, 5] }]}
                series={[
                    {
                        data: dat,
                    },
                ]}
                width={500}
                height={300}
            />
        </div>
    );
}
