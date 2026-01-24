import express from "express";
import Phone from "../models/Phone.js";

const router = express.Router();

router.post("/sell", async (req, res) => {
  try {
    const phone = new Phone(req.body);
    const savedPhone = await phone.save();
    res.status(201).json(savedPhone);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

router.get("/", async (req, res) => {
  try {
    const phones = await Phone.find().sort({ createdAt: -1 });
    res.json(phones);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

export default router;
