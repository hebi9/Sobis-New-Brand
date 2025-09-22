import { useEffect, useState } from "react";

const API_BASE_URL =
  window.location.hostname === "localhost"
    ? "http://localhost:8000"
    : "https://hebi.pythonanywhere.com";

export default function WhoWeAre() {
     const [description, setDescription] = useState("");

  useEffect(() => {
    const fetchDescription = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/api/who-we-are/`);
        const data = await response.json();
        console.log("Fetched data:", data.who_we_are[0].content);
        setDescription(data.who_we_are[0].content);
      } catch (err) {
        console.error("Error fetching description:", err);
      }
    };

    fetchDescription();
  }, []);
    return (
        <>
        <h2>¿Quiénes somos?</h2>
        <h3>SOBI’S DEV</h3>
        <section>
            <p>{description.split("\n").map((line, index) => (
                <span key={index}>
                    {line}
                    <br />
                </span>
                ))}
            </p>
        </section>
        </>
    );
}
