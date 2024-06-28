# ClimateWise

# Inspiration
I came across a quote that deeply moved me: 'By 2050, a further 24 million children are projected to be undernourished as a result of the climate crisis.' It made me reflect profoundly on the significant impact climate change has on our world." Melting ice caps and glaciers contribute to rising sea levels and warmer temperatures, threatening the availability of land for future generations. This inspired us to create an application that educates individuals about their carbon footprint, suggests ways to reduce it, and leverages AI technology to assist in these efforts, thereby promising a sustainable future for everyone.

# What it does
The app provides users with an overview of their carbon footprint based on their daily activities. It provides an intuitive textual response from which users can gain actionable insights.

# Key features include:

**Home Page**: Displaying a summary of the user's overall carbon footprint, along with actionable advice on reducing it.

![image](https://github.com/ketanmalempati/ClimateWise/assets/57043103/afafdec6-bebe-42da-b2c6-e43d63046e58)

**Interactive Chatbot**: Users can engage in voice or text conversations with an AI-driven chatbot to gain a deeper understanding of their carbon output and receive personalized suggestions.

![image](https://github.com/ketanmalempati/ClimateWise/assets/57043103/a8014020-c307-47fd-8771-055585416080)
![image](https://github.com/ketanmalempati/ClimateWise/assets/57043103/5cf843fa-06aa-472c-bfde-a99bdd2328bb)

**Receipt Analysis**: Users can upload images of their receipts, and the app utilizes AI to extract data and calculate the associated carbon footprint.

![image](https://github.com/ketanmalempati/ClimateWise/assets/57043103/8a8801a5-b6d7-4749-a53c-1247b595f0bf)

**Transport Tracker**: Users input their mode of transportation along with the travel duration and distance, and the app calculates the carbon emissions for these activities.

![image](https://github.com/ketanmalempati/ClimateWise/assets/57043103/b488b349-c319-4dc6-a440-088531ef9ac1)

Users can review detailed reports and insights to identify high-emission areas and explore ways to reduce their footprint without significantly altering their lifestyle.

![image](https://github.com/ketanmalempati/ClimateWise/assets/57043103/333750df-6218-4cb9-aa1c-258dc5a81fd1)

# How we built it

We utilized a blend of modern web technologies and advanced AI services:

Frontend: Developed using HTML, CSS, and JavaScript to ensure a responsive and user-friendly interface.
Backend: Implemented with Flask, which facilitates communication between the frontend and various AI models hosted on Hugging Face and other platforms.
AI Integration: We integrated Amazon Bedrock for inference with LLMs like Anthropic Claude 3, OpenAI's Whisper for speech-to-text capabilities, and Moondream2 for image-to-text conversions.
Data Storage: Utilized AWS S3 buckets for robust and scalable storage of images, audio files, and textual data.
Challenges we ran into
One significant challenge was the integration of the Whisper model for transcription, primarily due to compatibility issues with different versions of OpenAI's API. This required extensive testing and modifications to ensure stable functionality.
Building the front end was a little complex since we mainly focused on backend and machine learning models for projects.
Accomplishments that we're proud of
We are particularly proud of developing a tool that can significantly impact individuals' ecological footprints. By providing easy-to-understand data and actionable insights, we empower users to make informed decisions that contribute to global sustainability.

# What we learned
This project enhanced our skills in collaborative problem-solving and integrating multiple technologies into a seamless application. We gained deeper insights into the capabilities and practical applications of large language models and AI in environmental conservation.

# What's next for the project?
Looking ahead, we plan to:
Expand Device Integration: Enable syncing with smartphones and wearable devices to track fitness and travel data automatically.
Financial Integration: Connect with banking apps to analyze spending patterns and suggest more eco-friendly purchasing options.
Community Challenges: Introduce features that allow users to participate in challenges with friends or colleagues, fostering a competitive spirit to achieve the lowest carbon footprint.
Our goal is to continually evolve the app to include more features that will not only help individuals reduce their carbon footprint but also engage communities in collective environmental responsibility.

https://youtu.be/cifZWxIGiAY
