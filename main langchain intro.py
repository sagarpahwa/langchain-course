import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set")
if not OPENAI_API_BASE:
    raise ValueError("OPENAI_API_BASE is not set")


def main():
    print("Hello from langchain-course!")
    information = """
    CARS24 is an Indian multinational online used car marketplace headquartered in Gurgaon.[3] The company is considered among the four major organised players in the used car segment in India.[4]
    
    History
    CARS24 was founded in 2015 by Vikram Chopra, Mehul Agrawal, Gajendra Jangid and Ruchit Agarwal as a platform to buy and sell used cars.[5] In 2021, the company expanded its operations internationally in several countries, including the United Arab Emirates, Thailand and Australia.[6]  
    The CARS24 platform facilitates the transaction and has an offline presence.[7] Apart from selling used cars, the company's services include paperwork such as transferring the car to the name of the new owner which enables end-to-end transactions and offers an online auction platform to businesses looking to sell their pre-owned cars.[8] In 2019, the company started offering verified used cars where the company offered a buyback guarantee on the vehicles verified by inspection.[9]
    The company operates 202 branches across 73 cities in India as of 2019.[10] Apart from its own branches, the company has a tie-up with more than 10,000 channel partners across 230 cities in India.[8] The company touched 150,000 annual car sales in 2019.[5]

    Old logo of CARS24
    In May 2020, the company launched CARS24 Moto.[11] Cars24 Moto is a service which allows customers to sell used two-wheelers such as motorbikes, mopeds and scooters on its platform. It also launched a service offering vehicles inspection services at the customers location in place of their branch.[12][13]

    Funding and endorsements
    CARS24 raised US$50 million in Series A and Series B rounds combined. In 2018, it raised a further US$50 million in Series C round of funding.[14]
    CARS24 raised US$100 million in a Series D round of funding in 2019. Investors in the company include Sequoia Capital, Exor Seeds, partners of DST Global, Kingsway Capital, KCK and Unbound and Moore Strategic Ventures.[15] As a part of the series D round of funding, the company received an investment from cricketer Mahendra Singh Dhoni, who simultaneously became the company's brand ambassador.[16] Cars24 raised US$200 million in Series E round of funding in 2020 and became a unicorn startup as it was valued at over a $1 billion.[citation needed]
    Apart from Dhoni, actors Boman Irani,[17] Mandira Bedi and Nawazuddin Siddiqui have endorsed the company in commercial advertisements.[18]
    Cars24 became the primary and front-of-shirt sponsor of Sunrisers Hyderabad (SRH) for 2022 Indian Premier League. Cars24's sponsorship of SRH marks the first time that a company from the second-hand cars category has sponsored an IPL team.[19]

    Subsidiaries
    The company established Cars24 Financial Services as a subsidiary in 2019.[20] The company received an NBFC license from Reserve Bank of India in July 2019.[21] Cars24 Financial Services provides consumer loan facilities to car dealers and end customers in the used car segment across 50 cities in India.[20] In 2019-20 the company claimed to have disbursed loans worth ₹400 crore (equivalent to ₹497 crore or US$59 million in 2023).[22]
    """

    summary_template = f"""
    given the information {information} about a company I want you to create:
    1. a short summary
    2. 2 interesting facts about the company
    """

    summary_prompt_template = PromptTemplate(
        template=summary_template, input_variables=["information"]
    )
    # open_ai_llm = ChatOpenAI(temperature=0, model="openai/gpt-4o-mini")
    # chain = summary_prompt_template | open_ai_llm
    ollama_llm = ChatOllama(temperature=0, model="deepseek-r1:8b")
    chain = summary_prompt_template | ollama_llm
    response = chain.invoke(input={"information": information})
    print(response.content)


if __name__ == "__main__":
    main()
