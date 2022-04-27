import { useEffect, useState } from "react";
import NewsCard from "./NewsCard";

let countries = [
  "ae",
  "ar",
  "at",
  "au",
  "be",
  "bg",
  "br",
  "ca",
  "ch",
  "cn",
  "co",
  "cu",
  "cz",
  "de",
  "eg",
  "fr",
  "gb",
  "gr",
  "hk",
  "hu",
  "id",
  "ie",
  "il",
  "in",
  "it",
  "jp",
  "kr",
  "lt",
  "lv",
  "ma",
  "mx",
  "my",
  "ng",
  "nl",
  "no",
  "nz",
  "ph",
  "pl",
  "pt",
  "ro",
  "rs",
  "ru",
  "sa",
  "se",
  "sg",
  "si",
  "sk",
  "th",
  "tr",
  "tw",
  "ua",
  "us",
  "ve",
  "za",
];

function News() {
  const [country, setCountry] = useState("in");
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    setArticles([]);
    fetch(`https://newsapi.org/v2/top-headlines?country=${country}`, {
      headers: { "X-Api-Key": process.env.REACT_APP_API_KEY },
    })
      .then((response) => response.json())
      .then((fetchedData) => setArticles(fetchedData.articles))
      .catch(console.log);
  }, [country]);

  return (
    <div className="bg-gray-100">
      <div className="text-center">
        <div className="text-6xl mb-4">News</div>
        <label>Select Country : </label>
        <select
          onChange={(e) => {
            setCountry(e.target.value);
          }}
          value={country}
          className="border-2 border-gray-500 rounded w-20"
        >
          {countries.map((country) => {
            return <option value={country}>{country}</option>;
          })}
        </select>
      </div>

      <div className="flex justify-center gap-5 m-6 mx-40 flex-wrap">
        {articles.length !== 0
          ? articles.map((article) => {
              return <NewsCard {...article} />;
            })
          : "...Getting News"}
      </div>
    </div>
  );
}

export default News;
