import { useEffect, useState } from "react";

function useLocalStorage(key, defaultValue) {
  const [storageValue, setStorageValue] = useState(
    JSON.parse(localStorage.getItem(key)) || defaultValue
  );

  useEffect(() => {
    localStorage.setItem(key, storageValue);
  }, [key, storageValue]);

  return [storageValue, setStorageValue];
}

export default useLocalStorage;
