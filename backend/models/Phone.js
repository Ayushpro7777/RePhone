import mongoose from "mongoose";

const phoneSchema = new mongoose.Schema({
  brand: { type: String, required: true },
  model: { type: String, required: true },
  price: { type: Number, required: true },
  condition: { type: String, required: true },
  description: String,
  sellerName: { type: String, required: true },
  sellerPhone: { type: String, required: true },
  createdAt: { type: Date, default: Date.now }
});

export default mongoose.model("Phone", phoneSchema);
