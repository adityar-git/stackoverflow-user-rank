import React, { Component } from 'react';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar'
import Typography from '@material-ui/core/Typography'
import { makeStyles } from '@material-ui/core/styles';
import IconButton from '@material-ui/core/IconButton'
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import axios from 'axios'
import Container from '@material-ui/core/Container';
import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid';
import StarIcon from '@material-ui/icons/Star';


class App extends Component{
  constructor(props){
    super(props)
    this.state = {
      url:'',
      userdata:{},
      rank:0
    }
  }

  sendURL = (e) => {
    axios
    .get('http://localhost:8000/stack?url='+this.state.url)
    .then(res=> this.setState({userdata:res.data}))
  }

  handleChange = (e) => {
    this.setState({url:e.target.value})
  }

  render(){
    return (
      <div>
        <AppBar position="static">
          <Toolbar>
            <IconButton edge="start" aria-label="menu">
            </IconButton>
            <Typography variant="h6" >
              StackOverflow Scraper
            </Typography>
          </Toolbar>
        </AppBar>
        
        <Container maxWidthXl>
          <h3>Enter a valid stackoverflow user URL!</h3>
          <TextField
            id="url-field"
            label="Stackoverflow URL"
            placeholder="Stackoverflow URL"
            helperText=""
            margin="normal"
            fullWidth
            variant="outlined"
            onChange={this.handleChange}
          />
          <br/><br/>
          <Box component="span" m={1}>
            <Button variant="contained" color="primary" onClick={this.sendURL}>
              Get Rank!
            </Button>
          </Box>
          <div >
            <br/>
            {
              this.state.userdata.user_details && (
                <div>
                <div style={{width:'100%',padding:'10px', border:'1px solid black', textAlign:'center'}}>
                  <strong>
                    <span style={{color:'#3f51b5'}}>{this.state.userdata.user_details[0].display_name}</span> is in the top <span style={{color:'#3f51b5'}}>{this.state.userdata.Rank}%</span> of Melbourne Stackoverflow users based on reputation
                  </strong>
                </div><br/>
          
          <br/>
          <Grid container spacing={3}>
            <Grid item xs={3}>
              <img style={{width:'100%',height:'100%'}} src={this.state.userdata.user_details[0].profile_image} /><br/>
            </Grid>
            
            <Grid item xs={9}>
              <div style={{padding:'10px', fontSize:'20px'}}>
                <Grid container spacing={3}>
                  <Grid item xs={4}>
                    <center>
                      <StarIcon fontSize="large" style={{color:'#4e342e'}}></StarIcon>
                      <p><strong>{this.state.userdata.user_details[0].badge_counts.bronze}</strong></p>
                    </center>
                  </Grid>
                  <Grid item xs={4}>
                    <center>
                      <StarIcon fontSize="large" style={{color:'#424242'}}></StarIcon>
                      <p><strong>{this.state.userdata.user_details[0].badge_counts.silver}</strong></p>
                    </center>
                  </Grid>
                  <Grid item xs={4}>
                    <center>
                      <StarIcon  fontSize="large" style={{color:'#ffab40'}}></StarIcon>
                      <p><strong>{this.state.userdata.user_details[0].badge_counts.gold}</strong></p>
                    </center>
                  </Grid>
                </Grid>
              </div>
              <div style={{border:'1px solid black', padding:'10px'}}>
                
                    <div>
                      <p><strong>Reputation</strong>:{this.state.userdata.user_details[0].reputation}</p>
                      <p><strong>Employee</strong>:{this.state.userdata.user_details[0].is_employee}</p>
                      <p><strong>User ID</strong>:{this.state.userdata.user_details[0].user_id}</p>
                      <p><strong>Website URL</strong>:{this.state.userdata.user_details[0].website_url}</p>
                    </div>
                  
              </div>
            </Grid>

          </Grid>
          </div>
           )}
        </div>
        </Container>
        </div>
    )
  }
}

export default App;
