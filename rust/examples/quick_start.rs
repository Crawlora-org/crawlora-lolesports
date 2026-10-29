use crawlora_lolesports::{serde_json, Client, LolesportsScheduleParams};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .lolesports
        .schedule(LolesportsScheduleParams {
            hl: Some("en-US".to_owned()),
            ..Default::default()
        })
        .await?;
    let data: serde_json::Value = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
