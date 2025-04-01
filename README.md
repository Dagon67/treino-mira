# Treino Mira

Um aplicativo de treinamento de mira desenvolvido em Python usando Pygame. Projetado para ajudar jogadores a melhorar sua precisão, tempo de reação e habilidades de rastreamento em jogos.

## Características

- Interface gráfica moderna e intuitiva
- Múltiplos modos de treinamento:
  - **Estático**: Alvos fixos para treinar precisão básica
  - **Movimento**: Alvos em movimento para treinar rastreamento
  - **Reflexo**: Alvos que aparecem aleatoriamente para treinar tempo de reação
  - **Desafio**: Múltiplos alvos em movimento para treino avançado
- Sistema de pontuação e recordes
- Estatísticas detalhadas de desempenho
- Efeitos visuais e sonoros
- Configurações personalizáveis

## Requisitos

- Python 3.8 ou superior
- Pygame 2.5.0 ou superior

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Dagon67/treino-mira.git
cd treino-mira
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute o jogo:
```bash
python main.py
```

## Estrutura do Projeto

```
treino-mira/
├── main.py          # Arquivo principal do jogo
├── config.py        # Configurações do jogo
├── ui.py           # Interface do usuário
├── target.py       # Classe dos alvos
├── stats.py        # Sistema de estatísticas
├── assets/         # Arquivos de mídia
│   ├── hit.wav     # Som de acerto
│   └── miss.wav    # Som de erro
├── requirements.txt # Dependências
└── README.md       # Documentação
```

## Modos de Jogo

### Modo Estático
- Alvos fixos em posições aleatórias
- Foco em precisão e velocidade
- Ideal para iniciantes
- Treina cliques precisos

### Modo Movimento
- Alvos em movimento constante
- Treina habilidade de rastreamento
- Movimento previsível mas desafiador
- Velocidade configurável

### Modo Reflexo
- Alvos aparecem aleatoriamente
- Foco em tempo de reação
- Treina reflexos rápidos
- Intervalo aleatório entre alvos

### Modo Desafio
- Múltiplos alvos em movimento
- Combina todas as habilidades
- Dificuldade progressiva
- Modo mais desafiador

## Características Técnicas

### Interface Gráfica
- Design minimalista e funcional
- Feedback visual claro
- Animações suaves
- HUD informativo
- Menu intuitivo

### Sistema de Pontuação
- Rastreamento de acertos/erros
- Cálculo de precisão
- Recordes por modo
- Histórico de sessões

### Estatísticas
- Precisão por sessão
- Tempo médio de reação
- Total de acertos/erros
- Melhores pontuações
- Progresso ao longo do tempo

### Personalização
- Tamanho dos alvos
- Velocidade de movimento
- Cores e efeitos visuais
- Sensibilidade
- Som e volume

## Desenvolvimento

### Tecnologias Utilizadas
- Python 3.8+
- Pygame 2.5.0+
- JSON para armazenamento
- Módulos personalizados

### Arquitetura
- Orientação a objetos
- Código modular
- Fácil extensibilidade
- Bem documentado

### Performance
- Otimização de renderização
- Gestão eficiente de recursos
- Baixo consumo de memória
- FPS constante (60 FPS)

## Contribuindo

1. Fork o projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Próximas Atualizações

- [ ] Novos modos de jogo
- [ ] Sistema de conquistas
- [ ] Perfis de usuário
- [ ] Leaderboards online
- [ ] Customização avançada
- [ ] Modos de treino específicos
- [ ] Análise detalhada de desempenho
- [ ] Exportação de estatísticas


## Contato

 [@Dagon67](https://github.com/Dagon67)

Link do Projeto: [https://github.com/Dagon67/treino-mira](https://github.com/Dagon67/treino-mira)
