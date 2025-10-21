def fifo_page_replacement():
    print("=" * 50)
    print("FIFO Page Replacement Algorithm")
    print("=" * 50)
    
    
    page_string = input("Enter page reference string (space-separated): ")
    pages = list(map(int, page_string.split()))
    frame_size = int(input("Enter frame size: "))
    
  
    print(f"Page Reference String: {pages}")
    print(f"Frame Size: {frame_size}")
   
    
    frames = []
    page_faults = 0
    page_hits = 0
    fifo_index = 0 
    
    for i, page in enumerate(pages, 1):
        if page in frames:
            
            page_hits += 1
            print(f"Step {i}: Page {page} -> HIT | Frames: {frames}")
        else:
           
            page_faults += 1
            if len(frames) < frame_size:
              
                frames.append(page)
            else:
               
                frames[fifo_index] = page
                fifo_index = (fifo_index + 1) % frame_size
            print(f"Step {i}: Page {page} -> FAULT | Frames: {frames}")
    
    print("-" * 50)
    print(f"Total Page Faults: {page_faults}")
    print(f"Total Page Hits: {page_hits}")
    
    total_references = len(pages)
    hit_ratio = (page_hits / total_references) * 100
    fault_ratio = (page_faults / total_references) * 100
    
    print(f"Hit Ratio: {hit_ratio:.2f}%")
    print(f"Fault Ratio: {fault_ratio:.2f}%")

if __name__ == "__main__":
    fifo_page_replacement()
