from crewai import Agent, Task, TaskOutput
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
        task = Task(
            description="""Gere 10 temas para devocionais cristãos voltados para mulheres.
            Os temas devem ser relevantes e inspiradores.""",
            expected_output="Lista de temas devocionais",
            output=TaskOutput(
                description="Lista de temas devocionais",
                value="Lista de temas"
            )
        )
        themes = self.agent.execute_task(task)
        return [theme.strip() for theme in themes.split('\n') if theme.strip()]

    def generate_content(self, theme):
        devotional_task = Task(
            description=f"""Crie um devocional cristão sobre o tema: {theme}.
            O devocional deve incluir reflexões bíblicas e aplicações práticas.""",
            expected_output="Texto do devocional",
            output=TaskOutput(
                description="Texto do devocional",
                value="Devocional completo"
            )
        )
        
        prayer_task = Task(
            description=f"""Crie uma oração relacionada ao tema: {theme}.
            A oração deve ser pessoal e significativa.""",
            expected_output="Texto da oração",
            output=TaskOutput(
                description="Texto da oração",
                value="Oração completa"
            )
        )
        
        devotional = self.agent.execute_task(devotional_task)
        prayer = self.agent.execute_task(prayer_task)
        
        return {
            'devotional': devotional,
            'prayer': prayer
        }