import React, { useState } from 'react';
import axios from 'axios';
import './Chatbot.css';

function Chatbot() {
    const [query, setQuery] = useState('');
    const [responses, setResponses] = useState([]);

    const sendQuery = async () => {
        try {
            const response = await axios.post('http://127.0.0.1:5000/ask', { query });
            setResponses([...responses, { query, response: response.data.response }]);
            setQuery('');
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <div className="chatbot">
            <div className="chatbox">
                {responses.map((res, index) => (
                    <div key={index}>
                        <div className="userQuery">{res.query}</div>
                        <div className="botResponse">{res.response}</div>
                    </div>
                ))}
            </div>
            <input type="text" value={query} onChange={(e) => setQuery(e.target.value)} />
            <button onClick={sendQuery}>Send</button>
        </div>
    );
}

export default Chatbot;
