# Diagnóstico Tecnológico e Arquitetura de Referência - Inteceleri

Trabalho prático da disciplina de **Tópicos Especiais**  
Curso Superior de Tecnologia em **Análise e Desenvolvimento de Sistemas (ADS)**  
**IFRO Campus Porto Velho Calama**

---

## 📌 Escopo do Projeto
* **Polo Mapeado:** PCT Guamá (Belém-PA)
* **Caso de Estudo:** Inteceleri Tecnologia para a Educação
* **Foco Técnico:** Mitigação de gargalos de conectividade (*Offline-First*), restrição de hardware (2GB-3GB RAM) e concorrência massiva de sincronização escolar via mensageria assíncrona.

---

## 🛠️ Stack Arquitetural Proposta
* **Cliente Mobile:** Flutter + SQLite (Persistência local Offline-First)
* **Borda & Storage:** Firebase Storage + CDN (Distribuição de assets 3D compactados)
* **Back-End API:** Node.js (Express)
* **Fila / Mensageria:** Redis (BullMQ)
* **Banco Relacional:** PostgreSQL
