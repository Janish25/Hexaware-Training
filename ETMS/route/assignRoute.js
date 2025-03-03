const express = require('express');
const { assignTaskToEmployee } = require('../controller/assigncontroller');
    
const router = express.Router();

router.post("/employee/task", assignTaskToEmployee)
 
module.exports = router; 