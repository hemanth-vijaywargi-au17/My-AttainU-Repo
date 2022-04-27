function NewsCard(props) {
  
  let {
    source,
    author,
    title,
    description,
    url,
    urlToImage,
    publishedAt,
  } = props;

  return (
    <a
      className="w-96 shadow-lg rounded cursor-pointer transform hover:scale-105 transition-all ease-in-out"
      href={url}
    >
      <img src={urlToImage} alt="" className="rounded" />
      <div className=" bg-white px-6 py-4 flex flex-col gap-3">
        <div className="text-sm text-gray-500 flex justify-between">
          <span>{source.name}</span>
          <span>
            {new Date(publishedAt).toDateString()},{" "}
            {new Date(publishedAt).toLocaleTimeString()}
          </span>
        </div>
        <div className="font-semibold text-lg">{title}</div>
        <p className="line-clamp-4">{description}</p>
        <p className="text-right text-sm text-gray-500"> - {author}</p>
      </div>
    </a>
  );
}

export default NewsCard;
