from crewai.tools import BaseTool
import requests
import os


class ConsultingExternalAPI(BaseTool):
    name: str = "Searching Movie Information Tool"
    description: str = "Call a External API to get more information about a movie."
    api_key: str = os.getenv("TMDB_API_KEY")

    def _get_movie_details(self, movie_name: str, detail_type: str):
        if not movie_name or not detail_type:
            return None

        search_url = (
            f"https://api.themoviedb.org/3/search/movie?api_key={self.api_key}"
            f"&query={movie_name}"
        )
        response = requests.get(search_url)
        data = response.json()

        def stringfyText(type: str, movies: list) -> str:
            text = type
            for movie in movies:
                text += f"\n - {movie}"
            return text

        if data["results"]:
            movie_id = data["results"][0]["id"]
            if detail_type == "cast":
                credits_url = (
                    f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
                    f"?api_key={self.api_key}"
                )
                credits_response = requests.get(credits_url)
                credits_data = credits_response.json()
                cast_list = [member["name"] for member in credits_data["cast"]]
                return stringfyText("Elenco:", cast_list)

            elif detail_type == "synopsis":
                movie_details_url = (
                    f"https://api.themoviedb.org/3/movie/{movie_id}"
                    f"?api_key={self.api_key}"
                )
                movie_details_response = requests.get(movie_details_url)
                movie_details_data = movie_details_response.json()
                return stringfyText("Sinopse:", movie_details_data)

            elif detail_type == "rating":
                movie_details_url = (
                    f"https://api.themoviedb.org/3/movie/{movie_id}"
                    f"?api_key={self.api_key}"
                )
                movie_details_response = requests.get(movie_details_url)
                movie_details_data = movie_details_response.json()
                return stringfyText("Avaliação:", movie_details_data)

        return None

    def _get_popular_movies(self):
        popular_url = (
            f"https://api.themoviedb.org/3/movie/popular?api_key={self.api_key}"
        )
        response = requests.get(popular_url)
        data = response.json()
        popular_movies = [movie["title"] for movie in data["results"]]
        stringfy_popular_movies = "Filmes populares:"
        for movie in popular_movies:
            stringfy_popular_movies += f"\n - {movie}"
        return stringfy_popular_movies

    def _get_recommendation_by_genre(self, genre: str):
        if not genre:
            return None

        genre_url = (
            f"https://api.themoviedb.org/3/genre/movie/list?api_key={self.api_key}"
        )
        genre_response = requests.get(genre_url)
        genre_data = genre_response.json()
        genre_id = next(
            (
                g["id"]
                for g in genre_data["genres"]
                if g["name"].lower() == genre.lower()
            ),
            None,
        )

        if genre_id:
            recommendation_url = (
                f"https://api.themoviedb.org/3/discover/movie?api_key={self.api_key}"
                f"&with_genres={genre_id}"
            )
            recommendation_response = requests.get(recommendation_url)
            recommendation_data = recommendation_response.json()
            recommendations = [
                movie["title"] for movie in recommendation_data["results"]
            ]
            stringfy_recommendations = "Recomendações:"
            for movie in recommendations:
                stringfy_recommendations += f"\n - {movie}"
            return stringfy_recommendations

        return None

    def _get_similar_movies(self, movie_name: str):
        if not movie_name:
            return None

        search_url = (
            f"https://api.themoviedb.org/3/search/movie?api_key={self.api_key}"
            f"&query={movie_name}"
        )
        response = requests.get(search_url)
        data = response.json()

        if data["results"]:
            movie_id = data["results"][0]["id"]
            similar_url = (
                f"https://api.themoviedb.org/3/movie/{movie_id}/similar"
                f"?api_key={self.api_key}"
            )
            similar_response = requests.get(similar_url)
            similar_data = similar_response.json()
            similar_movies = [movie["title"] for movie in similar_data["results"]]
            similiar_movies_stringfy = "Filmes similares:"
            for movie in similar_movies:
                similiar_movies_stringfy += f"\n - {movie}"
            return similiar_movies_stringfy

        return None

    def _run(self, movie_name: str = None, genre: str = None, text: str = None) -> str:
        def exists_in_text(key_list):
            return any(item in text.lower() for item in key_list)

        stringfyResponse = ""

        if movie_name:
            stringfyResponse += self._get_similar_movies(movie_name) + "\n\n"
        if exists_in_text(["cast", "elenco"]):
            stringfyResponse += self._get_movie_details(movie_name, "cast") + "\n\n"
        if exists_in_text(["synopsis", "sinopse"]):
            stringfyResponse += self._get_movie_details(movie_name, "synopsis") + "\n\n"
        if exists_in_text(["rating", "avaliacao", "avaliação"]):
            stringfyResponse += self._get_movie_details(movie_name, "rating") + "\n\n"
        if exists_in_text(["popular"]):
            stringfyResponse += self._get_popular_movies() + "\n\n"
        if genre and exists_in_text(["recomend", "recomm"]):
            stringfyResponse += self._get_recommendation_by_genre(genre) + "\n\n"

        return stringfyResponse
