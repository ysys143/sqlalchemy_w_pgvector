import React, { useState } from 'react';
import { Send } from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Alert, AlertDescription } from "@/components/ui/alert";

const LegalChatbot = () => {
  const [question, setQuestion] = useState('');
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!question.trim()) return;

    setIsLoading(true);
    const newMessage = { type: 'user', content: question };
    setMessages(prev => [...prev, newMessage]);

    try {
      const response = await fetch('/chatbot', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question_content: question })
      });

      const data = await response.json();
      setMessages(prev => [...prev, { type: 'bot', content: data.answer }]);
    } catch (error) {
      setMessages(prev => [...prev, { 
        type: 'error', 
        content: '죄송합니다. 응답을 받아오는 중 오류가 발생했습니다.' 
      }]);
    }

    setIsLoading(false);
    setQuestion('');
  };

  return (
    <div className="container mx-auto max-w-4xl p-4">
      <Card className="w-full">
        <CardHeader>
          <CardTitle className="text-2xl font-bold text-center">
            건설 관련 정보 검색 챗봇
          </CardTitle>
        </CardHeader>
        <CardContent>
          <ScrollArea className="h-[500px] mb-4 p-4 rounded-lg border">
            {messages.length === 0 ? (
              <div className="text-center text-gray-500 mt-32">
                건설 관련 법률 및 규정 관련 질문을 입력해주세요.
              </div>
            ) : (
              messages.map((msg, idx) => (
                <div
                  key={idx}
                  className={`mb-4 ${
                    msg.type === 'user' ? 'flex justify-end' : 'flex justify-start'
                  }`}
                >
                  <div
                    className={`max-w-[80%] p-3 rounded-lg ${
                      msg.type === 'user'
                        ? 'bg-blue-500 text-white'
                        : msg.type === 'error'
                        ? 'bg-red-100 text-red-800'
                        : 'bg-gray-100 text-gray-800'
                    }`}
                  >
                    {msg.type === 'error' ? (
                      <Alert variant="destructive">
                        <AlertDescription>{msg.content}</AlertDescription>
                      </Alert>
                    ) : (
                      <div className="whitespace-pre-wrap">{msg.content}</div>
                    )}
                  </div>
                </div>
              ))
            )}
          </ScrollArea>

          <form onSubmit={handleSubmit} className="flex gap-2">
            <Textarea
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              placeholder="질문을 입력하세요..."
              className="flex-1"
            />
            <Button 
              type="submit" 
              disabled={isLoading}
              className="px-6"
            >
              {isLoading ? (
                <div className="w-6 h-6 border-2 border-white border-t-transparent rounded-full animate-spin" />
              ) : (
                <Send className="w-5 h-5" />
              )}
            </Button>
          </form>
        </CardContent>
      </Card>
    </div>
  );
};

export default LegalChatbot;