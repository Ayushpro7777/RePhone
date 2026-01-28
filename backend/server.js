import express from "express";
import cors from "cors";

const app = express();

app.use(cors());
app.use(express.json());

// test route
app.get("/", (req, res) => {
  res.send("RePhone backend running");
});

// ✅ phones API
app.get("/phones", (req, res) => {
  res.json([
    { name: "iPhone 12", price: "45000", condition: "Good" },
    { name: "Samsung S21", price: "32000", condition: "Excellent" },
    { name: "OnePlus 9", price: "28000", condition: "Very Good" }
  ]);
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log("Server running on port " + PORT);
});
