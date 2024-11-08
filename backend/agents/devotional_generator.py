from crewai import Agent
from langchain_openai import ChatOpenAI

class DevotionalGenerator:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.7
        )
        self.agent = Agent(
            role='Escritor Devocional',
            goal='Criar devocionais cristãos para mulheres',
            backstory="""Especialista em conteúdo cristão com experiência em 
            criar devocionais inspiradores e relevantes para mulheres cristãs.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def generate_themes(self):
        prompt = """Gere 10 temas para devocionais cristãos voltados para mulheres.
        Os temas devem ser relevantes e inspiradores."""
        
        themes = self.agent.execute_task(prompt)
        return [theme.strip() for theme in themes.split('\n') if theme.strip()]

    def generate_content(self, theme):
        devotional_prompt = f"""Crie um devocional cristão sobre o tema: {theme}.
        O devocional deve incluir reflexões bíblicas e aplicações práticas."""
        
        prayer_prompt = f"""Crie uma oração relacionada ao tema: {theme}.
        A oração deve ser pessoal e significativa."""
        
        devotional = self.agent.execute_task(devotional_prompt)
        prayer = self.agent.execute_task(prayer_prompt)
        
        return {
            'devotional': devotional,
            'prayer': prayer
        }