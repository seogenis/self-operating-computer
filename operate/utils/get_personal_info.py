from openai import OpenAI
client = OpenAI()

def get_personal_info(field):
    # with open('personal_info.txt', 'r') as file:
    #     personal_info = file.read()
    personal_info = """
        Sean Wu
        Email: seanwu2019@gmail.com
        Phone Number: (609)-216-6480
        Address: 6 Howell Court, Princeton Junction, NJ 08540
        LinkedIn: https://www.linkedin.com/in/seanwu2027/

        EDUCATION: Santa Clara University - Santa Clara, CA - Bachelor of Science in Computer Science, Jun 2027 The Lawrenceville School - Lawrenceville, NJ - High School Diploma, May 2023

        WORK EXPERIENCE:
        AYR - Machine Learning Engineer / Software Intern Princeton, NJ	  		  Jun 2023 - Present
        Led the research and integration of LLM / RAG Agent into internal Slack tools and Citibank business contracts workflow, generating an additional $1.5 million revenue in the coming year. 
        Achieved 99.9% accuracy in binary signature classification - surpassed industrying-leading technology by developing novel fusion model architecture between Vision Transformer and CNN
        Used CUDA, QLoRA, quantization, and pruning to reduce 1B LLM inference time by 60%. 
        Curated image/text data, trained TrOCR models used by IRS, BNY, and Leidos-Lockheed Martin.
        GPT Printshop - Co-founder Princeton NJ			   Jul 2023 - Present 
        Launched GenAI-based custom t-shirt startup; surpassed $10,000 revenue in one month.
        Developed business plan, communicated with clients, and scaled production.
        Stanford Seung Kim Lab - Research Intern Remote	Sep 2022 - May 2023
        Utilized GAL4/UAS expression system and enhancer traps to develop trans-genetic fly lines.
        Jefferson University Hospital - Research Intern Philadelphia, PA	Jun 2022 - Sep 2022
        Grant funded research on diabetic cardiac adipocytes; developed internal data processing pipeline.
        
        OTHER PROJECTS:
        Mechanistic Interpretability Researcher: Collaborated with Harvard Computer Society to reverse engineer GPT-2 and develop novel progress indicators for interpreting the model grokking and generalization phenomena. Utilized pruning analysis, TransformersLens, and WandB. 
        SCU RAG Chatbot Lead: Leading team of 6 for over 500 hours to create retrieval-based chatbot user experience for Santa Clara University with Langchain and custom LLM. Ongoing official integration and support with university IT, President, and Board of Regents. Accelerator incubated.
        Eye-Mouse Project Lead: Integrated Haar Cascades, Viola-Jones Algorithm, and CNN into eye-tracking mouse control disability accommodation system with standard webcams
        
        RELEVANT ACTIVITIES AND HONORS:
        Mindset Scholar; Grand Challenge Scholar; Ciocca Innovation Fellow; Bronco Venture Accelerator; 
        SCU First Year Math Competition - 3rd place;SCU First Years Engineering 1 Fair - 1st place; Abraham .P Hillman Prize in Mathematics;SCU Maker Design Challenge - 2nd place. 
        High School Programming Club: Head of Machine Learning Branch; taught Python; developed evolutionary algorithms from scratch to play Flappy Bird and surpassed Flappy Bird world record. 
        AI Collaborate: Head of Advanced Research and Collaborations; Taught Transformers and LLMs.
        Princeton Academy Alumni Teaching Program: Founder; Teach Python at middle school biweekly.

        SKILLS:
        Python, Java, C++, C, Javascript, Large Language Models(LLM), Transformers, Optical Character Recognition(OCR),  Computer Vision, Natural Language Processing(NLP), Pytorch, Keras, Pandas, Numpy, OpenCV, LangChain, Keras, TensorFlow, CUDA, HuggingFace, Retrieval Augmented Generation(RAG), AI Agents, Django, SQL, Docker, Sales, Data Science, Chinese, Spanish
        Hobbies: Wrestling, Soccer, Martial Arts, Philosophy, Poetry, Piano, Stargazing, Comedy, Maker Lab
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Use the provided personal information to help fill out an application form's specified field. Return the field's value in a single line. If the field is not found, return 'None'."},
            {"role": "user", "content": f"Here is my personal information for reference:\n{personal_info}\n\n\nPlease help me fill out the following field in a job application form: {field}"}
        ]
    )
    content = response.choices[0].message.content

    return content

