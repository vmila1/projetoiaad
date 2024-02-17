import mysql.connector
import streamlit as st
import pandas as pd
from datetime import datetime

# Conectando com o MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sqlsenha",
    database="quadrinhos_sql"
)
mycursor = mydb.cursor()

# Criando o app streamlit
def main():
    st.title("OPERAÇÕES CRUD COM MySQL")

    # Opções de CRUD a selecionar
    option = st.sidebar.selectbox("Select an Operation", ("Create", "Read", "Update", "Delete"))

    if option == "Create":
        # Opções de CRUD a selecionar
        option = st.sidebar.selectbox("Select an Operation", ("Create Quadrinho", "Create editora", "Create equipe_produção"))

        if option == "Create Quadrinho":
            st.subheader("Adicionar um quadrinho")

            quadrinhoID = st.text_input('Digite o ID do quadrinho')
            editoraID = st.text_input('Digite o ID da editora')
            equipeID = st.text_input('Digite o ID da equipe')
            tituloComic = st.text_input('Digite o nome do quadrinho')
            activeYears = st.text_input('Digite o período de ano que esteve ativo o quadrinho, ano de início até o ano que parou de lançar')
            issueTitle = st.text_input('Digite o título da edição ex: incrível hulk edição #30')
            publishDate = st.date_input('Digite a data de publicação', format="YYYY-MM-DD")
            publishDate = datetime.strftime(publishDate, "%Y-%m-%d") if publishDate else None
            issueDescription = st.text_area('Digite a descrição da edição')
            Format = st.text_input('Digite o formato, Comic, Webtoon, Manga etc.')
            Rating_Age = st.text_input('Digite a classificação etária em anos')
            Price = st.text_input('Digite o preço')

            if st.button("Adicionar quadrinho"):
                try:
                    
                    if tituloComic and editoraID and equipeID and activeYears and issueTitle and publishDate and issueDescription and Format and Rating_Age and Price:
                        # Executar a inserção com parâmetro
                        query = "INSERT INTO `comics` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        values = (quadrinhoID, tituloComic, editoraID, equipeID, activeYears, issueTitle, publishDate, issueDescription, Format, Rating_Age, Price)

                        mycursor.execute(query, values)

                        mydb.commit()
                        st.success("Quadrinho adicionado com sucesso!")
                    else:
                        st.warning("Por favor, preencha todos os campos antes de adicionar a equipe.")

                except mysql.connector.Error as err:
                    if err.errno == 1452:  # Número de erro para violação de chave estrangeira
                        st.error("Erro de Integridade Referencial: Verifique se os IDs de editora e equipe existem.")
                    elif err.errno == 1062: # Número de erro para violação de chave primária
                        st.error("Chave primária duplicada, coloque outro valor no ID do quadrinho")
                    elif err.errno == 1644: # Número de erro para data de lançamento maior que a data atual
                        st.error("Data de publicação inválida, coloque uma data que já tenha acontecido")
                    else:
                        st.error(f"Erro ao adicionar o quadrinho: {err}")
        
        elif option == "Create editora":
            st.subheader("Adicionar editoras")
            EditoraID = st.text_input('Digite o ID da editora')
            nomeEditora = st.text_input('Digite o nome da editora')
            paísEditora = st.text_input('Digite o país de origem da editora')
            anoCriacao = st.text_input('Digite o ano de criação da editora')

            if st.button("Adicionar editora"):

                try:
                    if nomeEditora and paísEditora and anoCriacao:
                        # Executar a inserção com parâmetros
                        query = "INSERT INTO `editora` VALUES (%s, %s, %s, %s)"
                        values = (EditoraID, nomeEditora, paísEditora, anoCriacao)

                        mycursor.execute(query, values)
                        mydb.commit()
                        st.success("Editora adicionada com sucesso!")
                    else:
                        st.warning("Por favor, preencha todos os campos antes de adicionar a equipe.")

                except mysql.connector.Error as err:
                    if err.errno == 1062: # Número de erro para violação de chave primária
                        st.error("Chave primária duplicada, coloque outro valor no ID da editora")
                    else:
                        st.error(f"Erro ao adicionar a editora: {err}")

        elif option == "Create equipe_produção":
            st.subheader("Adicionar uma equipe de arte")
            # Código para adicionar equipe de produção
            artistasID = st.text_input('Digite o ID da equipe de arte')
            Writer = st.text_input('Digite o nome do(a) escritor(a)')
            Penciler = st.text_input('Digite o nome do(a) desenhista')
            coverArtist = st.text_input('Digite o nome do(a) artista de capa')

            if st.button("Adicionar Equipe"):
                try:
                    if Writer and Penciler and coverArtist:
                        # Executar a inserção com parâmetros
                        query = "INSERT INTO `equipe_producao` VALUES (%s, %s, %s, %s)"
                        values = (artistasID, Writer, Penciler, coverArtist)

                        mycursor.execute(query, values)
                        mydb.commit()
                        st.success("Equipe adicionada com sucesso!")
                    else:
                        st.warning("Por favor, preencha todos os campos antes de adicionar a equipe.")

                except mysql.connector.Error as err:
                    if err.errno == 1062: # Número de erro para violação de chave primária
                        st.error("Chave primária duplicada, coloque outro valor no ID da equipe")
                    else:
                        st.error(f"Erro ao adicionar a equipe: {err}")


    elif option == "Read":
        st.subheader("Visualizar os quadrinhos")

        # Executa a query para selecionar todos os quadrinhos
        mycursor.execute("SELECT * FROM comics")
        result = mycursor.fetchall()

        # Mostra os dados usando o Pandas DataFrame
        df = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
        st.dataframe(df)
        
        st.subheader("Visualizar as editoras")

        # Executa a query para selecionar todas as editoras
        mycursor.execute("SELECT * FROM editora")
        result = mycursor.fetchall()

        # Mostra os dados usando o Pandas DataFrame
        df = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
        st.dataframe(df)
        
        st.subheader("Visualizar as equipes de produção")

        # Executa a query para selecionar todas as equipes de produção
        mycursor.execute("SELECT * FROM equipe_producao")
        result = mycursor.fetchall()

        # Mostra os dados usando o Pandas DataFrame
        df = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
        st.dataframe(df)
        
        st.subheader("Junção das 3 tabelas para melhor visualização das informações de cada comic")
        mycursor.execute("""
            SELECT comics.*, editora.nomeEditora, editora.paísEditora, editora.anoCriacao, equipe_producao.Writer, equipe_producao.Penciler, equipe_producao.coverArtist
            FROM comics
            JOIN editora ON comics.editoraID = editora.editoraID
            JOIN equipe_producao ON comics.equipeID = equipe_producao.equipeID
        """)
        result = mycursor.fetchall()
        df = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
        st.dataframe(df)
        
        st.subheader("Junção entre as tabelas editora e comics, agrupando os resultados por editoraID e média de preço por cada editora")
        # Executa a query para obter o número total de quadrinhos e a média de preço por editora
        mycursor.execute("""
            SELECT editora.nomeEditora, COUNT(comics.tituloComic) AS NumeroQuadrinhos, AVG(comics.Price) AS MediaPreco
            FROM editora
            LEFT JOIN comics ON editora.editoraID = comics.editoraID
            GROUP BY editora.editoraID
        """)
        result = mycursor.fetchall()

        # Mostra os dados usando o Pandas DataFrame
        df = pd.DataFrame(result, columns=["Nome da Editora", "Número de Quadrinhos", "Média de Preço"])
        st.dataframe(df)


    elif option == "Update":
    # Opções de CRUD a selecionar para Update
        update_option = st.sidebar.selectbox("Select Update Operation", ("Update Quadrinho", "Update Editora", "Update Equipe de Produção"))

        if update_option == "Update Quadrinho":
            st.subheader("Atualizar um quadrinho")

            # Mostrar todas os quadrinhos disponíveis
            mycursor.execute("SELECT * FROM comics")
            result = mycursor.fetchall()

            if not result:
                st.warning("Nenhum quadrinho encontrado no banco de dados para atualização.")
                return

            st.subheader("Quadrinhos Disponíveis para Atualização:")
            df = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
            selected_quadrinho_id_update = st.selectbox("Selecione o ID do quadrinho para atualização:", df["comicID"].tolist())

            if not selected_quadrinho_id_update:
                return

            # Viewer para mostrar informações do quadrinho ao selecionar o ID
            st.subheader(f"Informações do Quadrinho (ID: {selected_quadrinho_id_update}):")
            quadrinho_info_update = df[df["comicID"] == selected_quadrinho_id_update].iloc[0]
            st.write(quadrinho_info_update)

            st.subheader("Atualizar Informações do Quadrinho:")

            # Campos editáveis, incluindo comicID
            new_comicID = st.text_input('Digite o novo ID do quadrinho', selected_quadrinho_id_update)
            new_tituloComic = st.text_input('Digite o novo nome do quadrinho', quadrinho_info_update['tituloComic'])
            new_editoraID = st.text_input('Digite o novo ID da editora', quadrinho_info_update['editoraID'])
            new_equipeID = st.text_input('Digite o novo ID da equipe', quadrinho_info_update['equipeID'])
            new_activeYears = st.text_input('Digite o novo período de ano do quadrinho', quadrinho_info_update['activeYears'])
            new_issueTitle = st.text_input('Digite o novo título da edição', quadrinho_info_update['issueTitle'])
            new_publishDate = st.date_input('Digite a nova data de publicação', format="YYYY-MM-DD")
            new_publishDate = datetime.strftime(new_publishDate, "%Y-%m-%d") if new_publishDate else None
            new_issueDescription = st.text_area('Digite a nova descrição da edição', quadrinho_info_update['issueDescription'])
            new_Format = st.text_input('Digite o novo formato', quadrinho_info_update['Format'])
            new_Rating_Age = st.text_input('Digite a nova classificação etária em anos', quadrinho_info_update['Rating_Age'])
            new_Price = st.text_input('Digite o novo preço', quadrinho_info_update['Price'])

            if st.button("Atualizar quadrinho"):
                try:
                    mycursor.execute("START TRANSACTION")

                    # Executar a atualização com parâmetros apenas para o quadrinho selecionado
                    update_query = """
                        UPDATE comics
                        SET comicID=%s, tituloComic=%s, editoraID=%s, equipeID=%s, activeYears=%s,
                        issueTitle=%s, publishDate=%s, issueDescription=%s, Format=%s,
                        Rating_Age=%s, Price=%s
                        WHERE comicID=%s
                    """
                    update_values = (
                        new_comicID, new_tituloComic, new_editoraID, new_equipeID, new_activeYears,
                        new_issueTitle, new_publishDate, new_issueDescription, new_Format,
                        new_Rating_Age, new_Price, selected_quadrinho_id_update
                    )

                    mycursor.execute(update_query, update_values)

                    mydb.commit()
                    st.success("Quadrinho atualizado com sucesso!")

                except mysql.connector.Error as err:
                    mydb.rollback()
                    if err.errno == 1452:  # Número de erro para violação de chave estrangeira
                        st.error("Erro de Integridade Referencial: Verifique se os IDs de editora e equipe existem.")
                    elif err.errno == 1062:  # Número de erro para violação de chave primária
                        st.error("Chave primária duplicada, coloque outro valor no ID do quadrinho")
                    elif err.errno == 1644:  # Número de erro para data de lançamento maior que a data atual
                        st.error("Data de publicação inválida, coloque uma data que já tenha acontecido")
                    else:
                        st.error(f"Erro ao atualizar o quadrinho: {err}")

        
        elif update_option == "Update Editora":
            st.subheader("Atualizar uma editora")

            # Mostrar todas as editoras disponíveis
            mycursor.execute("SELECT * FROM editora")
            result_editora = mycursor.fetchall()

            if not result_editora:
                st.warning("Nenhuma editora encontrada no banco de dados para atualização.")
                return

            st.subheader("Editoras Disponíveis para Atualização:")
            df_editora = pd.DataFrame(result_editora, columns=[desc[0] for desc in mycursor.description])
            selected_editora_id_update = st.selectbox("Selecione o ID da editora para atualização:", df_editora["editoraID"].tolist())

            if not selected_editora_id_update:
                return

            # Viewer para mostrar informações da editora ao selecionar o ID
            st.subheader(f"Informações da Editora (ID: {selected_editora_id_update}):")
            editora_info_update = df_editora[df_editora["editoraID"] == selected_editora_id_update].iloc[0]
            st.write(editora_info_update)

            st.subheader("Atualizar Informações da Editora:")

            # Campos editáveis, incluindo EditoraID
            new_editoraID = st.text_input('Digite o novo ID da editora', str(selected_editora_id_update))
            new_nomeEditora = st.text_input('Digite o novo nome da editora', editora_info_update['nomeEditora'])
            new_paísEditora = st.text_input('Digite o novo país de origem da editora', editora_info_update['paísEditora'])
            new_anoCriacao = st.text_input('Digite o novo ano de criação da editora', editora_info_update['anoCriacao'])

            if st.button("Atualizar editora"):
                try:
                    mycursor.execute("START TRANSACTION")

                    # Executar a atualização com parâmetros
                    update_query_editora = """
                        UPDATE editora
                        SET editoraID=%s, nomeEditora=%s, paísEditora=%s, anoCriacao=%s
                        WHERE editoraID=%s
                    """
                    update_values_editora = (
                        new_editoraID, new_nomeEditora, new_paísEditora, new_anoCriacao, selected_editora_id_update
                    )

                    mycursor.execute(update_query_editora, update_values_editora)
                    mydb.commit()
                    st.success("Editora atualizada com sucesso!")

                except mysql.connector.Error as err:
                    mydb.rollback()
                    if err.errno == 1062:  # Número de erro para violação de chave primária
                        st.error("Chave primária duplicada, coloque outro valor no ID da editora")
                    else:
                        st.error(f"Erro ao atualizar a editora: {err}")

        elif update_option == "Update Equipe de Produção":
            st.subheader("Atualizar uma equipe de produção")

            # Mostrar todas as equipes de produção disponíveis
            mycursor.execute("SELECT * FROM equipe_producao")
            result_equipe = mycursor.fetchall()

            if not result_equipe:
                st.warning("Nenhuma equipe de produção encontrada no banco de dados para atualização.")
                return

            st.subheader("Equipes de Produção Disponíveis para Atualização:")
            df_equipe = pd.DataFrame(result_equipe, columns=[desc[0] for desc in mycursor.description])

            if 'equipeID' not in df_equipe.columns:
                st.warning("A coluna 'equipeID' não foi encontrada no DataFrame.")
                return

            selected_equipe_id_update = st.selectbox("Selecione o ID da equipe para atualização:", df_equipe["equipeID"].tolist())

            if not selected_equipe_id_update:
                return

            # Viewer para mostrar informações da equipe ao selecionar o ID
            st.subheader(f"Informações da Equipe de Produção (ID: {selected_equipe_id_update}):")
            equipe_info_update = df_equipe[df_equipe["equipeID"] == selected_equipe_id_update].iloc[0]
            st.write(equipe_info_update)

            st.subheader("Atualizar Informações da Equipe de Produção:")

            # Campos editáveis, incluindo equipeID
            new_equipeID = st.text_input('Digite o novo ID da equipe', selected_equipe_id_update)
            new_Writer = st.text_input('Digite o novo escritor da equipe', equipe_info_update['Writer'])
            new_Penciler = st.text_input('Digite o novo desenhista da equipe', equipe_info_update['Penciler'])
            new_coverArtist = st.text_input('Digite o novo artista da capa da equipe', equipe_info_update['coverArtist'])

            if st.button("Atualizar equipe de produção"):
                try:
                    mycursor.execute("START TRANSACTION")

                    # Executar a atualização com parâmetros
                    update_query_equipe = """
                        UPDATE equipe_producao
                        SET equipeID=%s, Writer=%s, Penciler=%s, coverArtist=%s
                        WHERE equipeID=%s
                    """
                    update_values_equipe = (
                        new_equipeID, new_Writer, new_Penciler, new_coverArtist, selected_equipe_id_update
                    )

                    mycursor.execute(update_query_equipe, update_values_equipe)
                    mydb.commit()
                    st.success("Equipe de produção atualizada com sucesso!")

                except mysql.connector.Error as err:
                    mydb.rollback()
                    if err.errno == 1062:  # Número de erro para violação de chave primária
                        st.error("Chave primária duplicada, coloque outro valor no ID da equipe")
                    else:
                        st.error(f"Erro ao atualizar a equipe de produção: {err}")

    elif option == "Delete":

        # Opções de CRUD a selecionar para Delete
        delete_option = st.sidebar.selectbox("Select Delete Operation", ("Delete Quadrinho", "Delete Editora", "Delete Equipe de Produção"))

        if delete_option == "Delete Quadrinho":
            st.subheader("Deletar um quadrinho")

            # Mostrar todas os quadrinhos disponíveis
            mycursor.execute("SELECT * FROM comics")
            result = mycursor.fetchall()

            if result:
                st.subheader("Quadrinhos Disponíveis:")
                df = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
                selected_quadrinho_id = st.selectbox("Selecione o ID do quadrinho:", df["comicID"].tolist())

                # Viewer para mostrar informações do quadrinho ao selecionar o ID
                if selected_quadrinho_id:
                    st.subheader(f"Informações do Quadrinho (ID: {selected_quadrinho_id}):")
                    quadrinho_info = df[df["comicID"] == selected_quadrinho_id].iloc[0]
                    st.write(quadrinho_info)

                    confirm_delete = st.radio("Realmente deseja deletar?", ("Sim", "Não"), key="confirm_delete")

                    if confirm_delete == "Sim" and st.button("Deletar"):
                        try:
                            # Excluir o quadrinho
                            mycursor.execute("DELETE FROM comics WHERE comicID = %s", (selected_quadrinho_id,))
                            mydb.commit()

                            st.success("Quadrinho excluído com sucesso!")
                        except Exception as e:
                            st.error(f"Erro ao excluir quadrinho: {e}")
                    elif confirm_delete == "Não":
                        st.warning("Exclusão cancelada.")
            else:
                st.warning("Nenhum quadrinho encontrado no banco de dados.")

        elif delete_option == "Delete Editora":
            st.subheader("Deletar uma editora")

            # Mostrar todas as editoras disponíveis
            mycursor.execute("SELECT * FROM editora")
            result = mycursor.fetchall()

            if result:
                st.subheader("Editoras Disponíveis:")
                df = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
                selected_editora_id = st.selectbox("Selecione o ID da editora:", df["editoraID"].tolist())

                # Viewer para mostrar informações da editora ao selecionar o ID
                if selected_editora_id:
                    st.subheader(f"Informações da Editora (ID: {selected_editora_id}):")
                    editora_info = df[df["editoraID"] == selected_editora_id].iloc[0]
                    st.write(editora_info)

                    confirm_delete = st.radio("Realmente deseja deletar?", ("Sim", "Não"), key="confirm_delete")

                    if confirm_delete == "Sim" and st.button("Deletar"):
                        try:
                            # Obter os IDs dos quadrinhos associados à editora
                            mycursor.execute("SELECT comicID FROM comics WHERE editoraID = %s", (selected_editora_id,))
                            quadrinho_ids = [row[0] for row in mycursor.fetchall()]

                            # Excluir os quadrinhos associados
                            for quadrinho_id in quadrinho_ids:
                                mycursor.execute("DELETE FROM comics WHERE comicID = %s", (quadrinho_id,))

                            # Excluir a editora
                            mycursor.execute("DELETE FROM editora WHERE editoraID = %s", (selected_editora_id,))
                            mydb.commit()

                            st.success("Editora e Quadrinhos associados excluídos com sucesso!")
                        except Exception as e:
                            st.error(f"Erro ao excluir editora: {e}")
                    elif confirm_delete == "Não":
                        st.warning("Exclusão cancelada.")
            else:
                st.warning("Nenhuma editora encontrada no banco de dados.")

        elif delete_option == "Delete Equipe de Produção":
            st.subheader("Deletar uma equipe de produção")

            # Mostrar todas as equipes de produção disponíveis
            mycursor.execute("SELECT * FROM equipe_producao")
            result = mycursor.fetchall()

            if result:
                st.subheader("Equipes de Produção Disponíveis:")
                df = pd.DataFrame(result, columns=[desc[0] for desc in mycursor.description])
                selected_equipe_id = st.selectbox("Selecione o ID da equipe de produção:", df["equipeID"].tolist())

                # Viewer para mostrar informações da equipe ao selecionar o ID
                if selected_equipe_id:
                    st.subheader(f"Informações da Equipe de Produção (ID: {selected_equipe_id}):")
                    equipe_info = df[df["equipeID"] == selected_equipe_id].iloc[0]
                    st.write(equipe_info)

                    confirm_delete = st.radio("Realmente deseja deletar?", ("Sim", "Não"), key="confirm_delete")

                    if confirm_delete == "Sim" and st.button("Deletar"):
                        try:
                            # Obter os IDs dos quadrinhos associados à equipe
                            mycursor.execute("SELECT comicID FROM comics WHERE equipeID = %s", (selected_equipe_id,))
                            quadrinho_ids = [row[0] for row in mycursor.fetchall()]

                            # Excluir os quadrinhos associados
                            for quadrinho_id in quadrinho_ids:
                                mycursor.execute("DELETE FROM comics WHERE comicID = %s", (quadrinho_id,))

                            # Excluir a equipe de produção
                            mycursor.execute("DELETE FROM equipe_producao WHERE equipeID = %s", (selected_equipe_id,))
                            mydb.commit()

                            st.success("Equipe de Produção e Quadrinhos associados excluídos com sucesso!")
                        except Exception as e:
                            st.error(f"Erro ao excluir equipe de produção: {e}")
                    elif confirm_delete == "Não":
                        st.warning("Exclusão cancelada.")
            else:
                st.warning("Nenhuma equipe de produção encontrada no banco de dados.")

if __name__ == "__main__":
    main()