from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return '''<p><strong><P><strong><font size="6">Bem-vindo ao meu currículo online!
</font></strong></p> 
<p>Meu nome é Ivo Aragão, sou um Desenvolvedor Junior com habilidades 
em Java Springboot e JavaScript Nodejs, e estou localizado em Varzea Alegre, 
Ceará, Brasil.</p>

<p><p>Este currículo foi criado para compartilhar informações sobre minha 
experiência, formação acadêmica e habilidades técnicas. Sinta-se à vontade 
para explorar as diferentes seções abaixo:</p></p>


<p><a href="{}">/sobre:</a> Página sobre mim, onde 
compartilho informações mais detalhadas 
sobre minha formação acadêmica, habilidades e objetivos de carreira.</p>
<p><a href="{}">/experiencia:</a> Página com minha 
experiência profissional, onde descrevo as 
empresas que trabalhei e os projetos em que trabalhei.</p>
<p><a href="{}">/formacao:</a> Página com minha formação
 acadêmica, onde compartilho minhas 
graduações e cursos relevantes.</p>
<p><a href="{}">/contato:</a> Página com meus contatos, 
onde você pode encontrar meu e-mail e outras informações de contato.</p>
<p>Sinta-se à vontade para entrar em contato comigo se tiver alguma pergunta 
ou se quiser saber mais sobre minhas habilidades e experiência. Estou animado 
para conectar e explorar novas oportunidades juntos!</p></p>
'''.format(url_for('sobre'), url_for('experiencia'), 
url_for('formacao'), url_for('contato'))

 
@app.route('/sobre')
def sobre():
    return '''<P><strong><font size="6">Sobre</font></strong></p>
<p>Olá!</p>   
<p>Me chamo Ivo Aragão e tenho 30 anos. Sou Bacharel em
Administração e atualmente estou no 6º período de Sistemas da
Informação no IFCE – INSTITUTO FEDERAL DE EDUCAÇÃO
CIÊNCIA E TECNOLOGIA DO CEARÁ onde realmente
encontrei minha verdadeira motivação. A área da programação
é simplesmente fantástica e estou a cada dia aprendendo mais e
mais sobre esse universo tecnológico. Estou sempre focado em
melhorar o meu portfolio através de cursos e projetos para aprender
e contribuir de todas as formas para o crescimento da empresa.</p>
<p><a href="{}">/home</a>
'''.format(url_for('home'))
@app.route('/experiencia')
def experiencia():
    return '''<P><strong><font size="6">Experiencia</font></strong></p>
Embora eu não tenha experiência direta nesta área, estou 
confiante em minha capacidade de aprender rapidamente e aplicar minhas 
habilidades de resolução de problemas. Todos os dias estou aprendendendo mais,
trabalho em equipe e liderança para contribuir positivamente para 
a equipe e alcançar resultados excepcionais.<p><a href="{}">/home</a>
 '''.format(url_for('home'))
@app.route('/formacao')
def formacao():
    return '''<P><strong><font size="6">Formação</font></strong></p>
<p><strong>Estou estudando:</strong></p>
<p>- JAVA 
<p>- PYTHON </p>
<p>- BANCO DE DADOS </p>
<p>- JAVASCRIPT</p></p>
<p><strong>Habilidades interpessoais:</strong></p>
<p>- Aprendo rápido</p>
<p>- Trabalho em equipe</p>
<p>- Organização</p>
<p>- Criatividade</p>
<p>- Dedicação</p>
<p>- Positividade</p></p>
<p><strong>Formação acadêmica</strong></p>
<p>Instituto Federal de Educação, Ciência e Tecnologia do Ceará
Bacharelado, Tecnologia em Tecnologia da Informação/Sistemas da
Informação · (janeiro de 2020 - dezembro de 2023)</p>
<p>UniLeão
Bacharelado em Administração, Administração e Negócios · (janeiro de
2011 - dezembro de 2015)</p>
<p><strong>Principais competências</strong></p>
<p>Spring Framework</p>
<p>Programação orientada a objetos
(POO)</p>
<p>Spring web</p>
<p>MongoDB</p>
<p>NodeJs</p></p>
<p><strong>Certifications</p></strong>
<p>Java Básico</p> 
<p>Programação Orientada a Objeto 
Orange Tech + | BackEnd</p>
<p>JAVA COMPLETO</p>
<p>PROGRAMAÇÃO ORIENTADA A
OBJETOS + PROJETOS </p>
<p>Sistema web de vendas com
gerador de relatórios e gráficos.
(Fullstack NEXT.JS + Spring Boot,
React, TS e Jasper Reports.)</p>
<p>NodeJs-Udemy</p><p><a href="{}">/home</a>
'''.format(url_for('home'))
@app.route('/contato')
def contato(): 
    return ''' <P><strong><font size="6">Contato</font></strong></p>

<p>ivoaragao4@gmail.com</p>
<p>www.linkedin.com/in/ivoaragão-50a3a722b (LinkedIn)</p>
<p>github.com/Ivo-Aragao (Portfolio)</p><p><a href="{}">/home</a>

'''.format(url_for('home'))
if __name__ == '__main__':
    app.run()