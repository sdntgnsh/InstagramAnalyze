import React, { useState } from 'react';
import axios from 'axios';
import { PaperAirplaneIcon, UserCircleIcon } from '@heroicons/react/solid';

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const handleSend = async () => {
    if (input.trim() === "") return;

    const userMessage = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);

    try {
      const response = await axios.post('http://127.0.0.1:5000/chat', { message: input });
      const serverMessage = { sender: "server", text: response.data.reply };
      setMessages((prev) => [...prev, serverMessage]);
    } catch (error) {
      console.error("Error connecting to server:", error);
    }

    setInput("");
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      handleSend();
    }
  };

  return (
    <div className="flex flex-col h-screen bg-gray-900 text-white">
      {/* Header */}
      <header className="bg-gray-800 text-center p-4 font-bold text-xl">
        Vaitalitics
      </header>

      {/* Chat Body */}
      <div className="flex-1 overflow-y-scroll p-4 space-y-4">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`flex items-center ${
              msg.sender === "user" ? "justify-end" : "justify-start"
            }`}
          >
            {msg.sender === "server" && (
              <UserCircleIcon className="h-8 w-8 text-gray-400 mr-2" />
            )}
            <div
              className={`p-3 rounded-lg max-w-xs ${
                msg.sender === "user"
                  ? "bg-blue-600 text-white"
                  : "bg-gray-700 text-white"
              }`}
            >
              {msg.text}
            </div>
            {msg.sender === "user" && (
              <UserCircleIcon className="h-8 w-8 text-blue-400 ml-2" />
            )}
          </div>
        ))}
      </div>

      {/* Footer */}
      <div className="flex items-center p-4 bg-gray-800">
        <input
          type="text"
          placeholder="Type a message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
          className="flex-1 p-2 rounded-full bg-gray-700 border-none text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <button
          onClick={handleSend}
          className="ml-2 p-2 bg-blue-600 rounded-full hover:bg-blue-700"
        >
          <PaperAirplaneIcon className="h-6 w-6 transform rotate-90 text-white" />
        </button>
      </div>
    </div>
  );
}

export default App;
