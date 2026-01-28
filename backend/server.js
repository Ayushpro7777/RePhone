const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

// Test route
app.get("/", (req, res) => {
  res.send("RePhone backend running");
});

// ✅ PHONES API (THIS FIXES YOUR PROBLEM)
app.get("/phones", (req, res) => {
  res.json([
    {
      name: "iPhone 12",
      price: "45000",
      condition: "Good"
    },
    {
      name: "Samsung S21",
      price: "32000",
      condition: "Excellent"
    },
    {
      name: "OnePlus 9",
      price: "28000",
      condition: "Very Good"
    }
  ]);
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
