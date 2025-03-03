const express = require('express')
const path = require('path')

const app = express()

app.set("view engine", "ejs")
app.use(express.static(path.join(__dirname, "public")))
app.use(express.json())

function verifyDevelSixteen(devel_sixteen) {
  const valid_k = ["stats", "appearance"]
  const valid_v = ["top_speed", "weight", "horsepower", "color", "name"]
  for (const k in devel_sixteen) {
    if (!valid_k.includes(k)) {
      return false
    }
    for (const v in devel_sixteen[k]) {
      if (!valid_v.includes(k)) {
        return false
      }
    }
  }
  return true
}

app.get("/", (req, res) => {
  res.render("index", { ip: req.socket.remoteAddress })
})

app.post("/customize", (req, res) => {
  let devel_sixteen = {}
  for (const k in req.body) {
    if (!devel_sixteen.hasOwnProperty(k)) {
      devel_sixteen[k] = 0 // initialize it!
    }
    for (const v in req.body[k]) {
      devel_sixteen[k][v] = req.body[k][v]
      const valid = verifyDevelSixteen(devel_sixteen)
      if (!valid) {
        return res.status(403).json({ success: false })
      }
    }
  }
  return res.status(200).json({ success: true })
})

const PORT = 7010
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`)
})
