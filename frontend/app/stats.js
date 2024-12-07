
'use client'
import { LineChart } from '@mui/x-charts/LineChart';
import { test } from './data';
import { useEffect, useState } from 'react';

export default function Stats() {
    const [dat, changedat] = useState([0,0,0,0,0]);

    async function fetchData() {
        try {
            const dat = await test();
            changedat(dat);
        } 
        catch (error) {
            console.error("Error in fetchData function:", error);
        }
    }
    useEffect(() => {
        
       
    }, []);
    return (
        <div className=" p-5 bg-white min-w-[500px] rounded-lg shadow-md transition-transform transition-shadow hover:shadow-custom hover:translate-y-[-4.30px]">
            <div className='flex justify-between'> Stats 
            <select className="ml-2 p-1 border rounded">
                    <option value="option1">Option 1</option>
                    <option value="option2">Option 2</option>
                    <option value="option3">Option 3</option>
                </select>
            </div>
            <LineChart
                xAxis={[{ data: [1, 2, 3, 4, 5] }]}
                series={[
                    {
                        data: [dat[0], dat[1], dat[2], dat[3], dat[4]],
                        
                    },
                ]}
                width={500}
                height={300}
            />
        </div>
    );
}