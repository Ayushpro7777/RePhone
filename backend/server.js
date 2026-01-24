import express from "express";
import mongoose from "mongoose";
import dotenv from "dotenv";
import cors from "cors";
import phoneRoutes from "./routes/phoneRoutes.js";

dotenv.config();

const app = express();

app.use(cors());
app.use(express.json());

app.use("/api/phones", phoneRoutes);

async function startServer() {
  try {
    await mongoose.connect(process.env.MONGO_URI);
    console.log("MongoDB connected ho gaya ✅");

    const PORT = process.env.PORT || 5000;
    app.listen(PORT, () => {
      console.log(`Server running on port ${PORT}`);
    });
  } catch (err) {
    console.log("MongoDB connection failed ❌", err.message);
  }
}

startServer();

app.get("/", (req, res) => {
  res.send("RePhone Backend Running 🚀");
});
