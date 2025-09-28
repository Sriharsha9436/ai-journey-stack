import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import axios from "axios";

dotenv.config();

const app = express();
app.use(cors());
app.use(express.json());

app.post("/ask", async (req, res) => {
  const { query } = req.body;

  if (!query) {
    return res.status(400).json({ error: "Query is required" });
  }

  const payload = {
    chat_input: query,
    chat_history: [],
    top_k: 5
  };

  try {
    const response = await axios.post(
      process.env.AZURE_PROMPTFLOW_URL!,
      payload,
      {
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${process.env.AZURE_PROMPTFLOW_API_KEY}`,
          "azureml-model-deployment": process.env.AZURE_PROMPTFLOW_DEPLOYMENT!
        }
      }
    );

    console.log("✅ Prompt Flow response:", response.data);
    res.json({ answer: response.data });
  } catch (error: any) {
    console.error("❌ Error calling Prompt Flow:", error.message);
    res.status(403).json({ error: "Access denied. Check API key and deployment name." });
  }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`✅ Secure AI Chat API running on port ${PORT}`);
});